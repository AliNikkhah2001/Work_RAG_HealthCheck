# Work_RAG_HealthCheck

Static GitHub Pages dashboard for Dana RAG production health.

**Live:** https://alinikkhah2001.github.io/Work_RAG_HealthCheck/

## Hourly publish (GPU host)

The `gpu-health-report.timer` (every 1h, aligned with metrics push) writes:

| Path | Contents |
|------|----------|
| `runs/*.json` | Per-run status, services, random FAQ QA, latency, host, Jenkins |
| `metrics/status.json` | Live badge (`HEALTHY` / …) |
| `metrics/series.json` | Rolling hourly points |
| `logs/<run>/screenshots/` | Jenkins login, KB manager, WebUI main/alt, manager `:9000`, … (10s settle; auto-pruned ≤3 runs & ≤24h) |

### New dashboard panels

- **Jenkins & images** — auth + image freshness (none missing / none stale) + snapshot stamps
- **Latency** — retrieval / generation / E2E from random FAQ QA (`audit.stage_timing_ms` + KB `stage_ms`) + trend sparkline
- **Host resources** — ports, disk, RAM, NVIDIA GPU + trend
- **Endpoints** — collapsible one-line explainers
- **History** — heatmaps **per device** (Production / Dev / Stage)
- **Single reports** — collapsed by default; expand for metrics + screenshots

### Random QA

Each report samples **10** FAQ pairs (`q`+`a`) from the canned KB pack and re-rolls every run.

### KB version

Pack pins are semver-normalized (`schemas/v1.0.1.yaml` ≡ `1.0.1`) so false pack “discrepancies” no longer trip the badge when the corpus matches.

### Related automation (umbrella repo)

- `[ci snapshot]` — freeze images under `/splunk-data/production/snapshots/<stamp>/`
- `[ci heal]` / `[ci force-heal]` / `[ci heal:STAMP]` — restore tested snapshot from any laptop commit
- `gpu-webui-watch.timer` — hourly compare `components/webui` pin vs `Work_RAG-WebUI` tip; Multibranch scan (parent gitlink + `[ci prod]` still required to rebuild new WebUI)

See `deploy/monitor/README.md` and `deploy/jenkins/README.md` in `Work_Credit-RAG_Phase1`.

## Jenkins forensics & QA samples

Published by the umbrella hourly reporter (`Work_Credit-RAG_Phase1` `scripts/monitor/` + `gpu_full_recover_report.sh`):

| Path | Contents |
|---|---|
| `logs/<run>/e2e/random_qa.json` | Full FAQ sample questions + `generation.answer_preview` |
| `logs/<run>/dashboard.html` | Per-run detail; QA cards render from `random_qa.json` |
| `logs/<run>/meta/jenkins_status.json` | Auth, job, image freshness, `build_ok`, reasons |
| `logs/<run>/meta/jenkins/consoleText.txt` | Truncated Jenkins console for the last completed build |
| `logs/<run>/meta/jenkins/console_excerpt.txt` | Filtered docker/npm/ERROR/coverage-gate lines |
| `logs/<run>/meta/jenkins/stages.json` / `wfapi.json` | Pipeline stage dump when the controller exposes it |
| `logs/<run>/meta/jenkins/diagnosis.json` | Heuristic labels (e.g. stage controller on `main` vs real image build failure) |

The Pages home dashboard links to the newest console artifacts when present.
A red `last_build_FAILURE` with label `coverage_gate_stage_controller_on_main` means the
laptop/stage Jenkins refused to verify `main` — it is not proof that `rag-webui` npm/Docker failed.
Prod image builds require GPU job `dana-rag-prod` on `main` with `[ci prod]` / `[ci auto]`.

### Known failure: Build images / docker CLI (2026-11-16)

**Symptom in `meta/jenkins/`:** `docker: command not found`, or later
`unknown shorthand flag: 'f' in -f` on every `docker compose build` attempt.
Health Pages may still show stack **HEALTHY** (apps up) while `dana-rag-prod`
`last_build_FAILURE` / `docker_compose_build_failed`.

**Root cause (not “merges missing from git”):**
1. Umbrella `origin/main` already had PRs **#95/#98/#99/#100** (static CLI scripts +
   h200.yml sock-only) — `git pull` alone does **not** recreate the controller.
2. `dana-jenkins-prod` was last started with only `docker-compose.yml` +
   `docker-compose.gpu.yml` (**missing `docker-compose.h200.yml`**), still on an
   image **without** `/usr/local/bin/docker`.
3. Host `/usr/bin/docker` bind-mounts are dynamically linked → inside the
   container they look like `command not found` (ENOENT on ld-linux). Do **not**
   remount the host binary.
4. CI self-heal (`ci_resolve_docker.sh`) sometimes fetched a static `docker` into
   `.ci-bin/` **without** the compose plugin → `unknown shorthand flag: 'f'`.

**Host fix (GPU):** bake static CLI into `dana-jenkins:production`, recreate with
**all three** compose files (see umbrella `components/server-setup/imagebugfix.txt`
and `deploy/jenkins/README.md`). Verify:
`docker exec dana-jenkins-prod bash -c 'ldd /usr/local/bin/docker || true; docker compose version'`
→ static (“not a dynamic executable”) + Compose v2.

**Submodules will not “appear” on this host until:** tip is merged on the child
repo **and** the umbrella gitlink on `main` is bumped with `[ci prod]`/`[ci auto]`,
**and** Build images can run (this docker CLI fix). Watchers alone do not advance pins.


### Known failure: long-thread LLM «خطا در پردازش درخواست.» (2026-11-16)

**Not classic VRAM OOM.** TRT on GPU1 returns HTTP 400 when prompt_len > `max_seq_len` 8192
(`default_max_tokens` negative). GPU0 was idle (~140 GiB free).

**Mitigation now live:** Manager `:9000` fails over to **llama.cpp Q4** on GPU0 `:8080`
(`n_ctx=16384`). See Server-Setup `docs/ops/llm-fallback-gpu0.md`. Check
`GET http://127.0.0.1:9000/admin/fallback/status` and TRT log for overflow 400s.

