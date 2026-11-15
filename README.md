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

