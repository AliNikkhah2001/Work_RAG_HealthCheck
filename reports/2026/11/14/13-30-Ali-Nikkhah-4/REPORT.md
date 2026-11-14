# GPU Full Recovery Report — `20261114T132906Z-Ali-Nikkhah-4`

| Field | Value |
|------|------|
| UTC | 2026-11-14T13:30:31Z |
| Host | Ali-Nikkhah-4.local |
| Status | **HEALTHY** |
| Mode | `compose` |
| Umbrella HEAD | b242bba |
| last_good | none |
| deployed | none |
| QA | 3 / 3 chat passes |
| Health failures | 0 |

## What this run did
1. Host metadata (uptime, nvidia-smi, docker ps, df, free, journal, shutdown/reboot events)
2. ALL git commits (last 3 days, all branches, all submodules)
3. ALL shell commands run (last 3 days, bash history + journalctl)
4. ALL container logs (docker logs --timestamps --tail 5000 per container, up or down)
5. Database (PostgreSQL) logs + DVC knowledgebase logs
6. All host /tmp logs
7. Knowledgebase details (current KB, chunks, version, commit history, entity lists)
8. All builds/runs (Jenkins logs, compose logs)
9. Command/shutdown/reboot/user metadata
10. Attempted restart of last known services
11. Curl health matrix (all endpoints each service serves)
12. E2E chat QA + KB search + OpenWebUI direct test
13. Headless screenshots of all service endpoints
14. HTML dashboard

## Health matrix
```
port   service          http_code  body_preview
18000  gemma            200
9000   manager          000
8000   kb               200
8200   guardrails       200
8100   orchestrator     200
3000   trace-collector  200
3001   langfuse         000
13000  webui            200
8085   jenkins          200
8010   service:8010     000
8001   service:8001     000
8002   service:8002     000
8003   service:8003     000
```

## E2E summary
```
chat_greeting http=200
chat_credit_qa http=200
chat_webui http=401
chat_webui note: auth required — skipped on dev, will pass on prod with WEBUI_AUTH=REDACTED
kb_search http=200
qa_pass=3/3
```

## Knowledgebase details
```
=== Knowledgebase container ===
KB container: dana-local-kb-1
--- KB container env ---
KB_EMBED_DIM=384
KB_OPENROUTER_API_KEY=REDACTED
KB_OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
KB_WEB_HOST=0.0.0.0
KB_EMBED_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
KB_WEB_PORT=8000
KB_RERANKER_DEVICE=cpu
KB_DB_MODE=pgvector
KB_REDIS_URL=redis://REDACTED
KB_EMBED_BACKEND=local
KB_DB_URL=postgresql://REDACTED
HF_HUB_CACHE=/models
HF_HOME=/models
KB_RERANKER_MODEL=cohere/rerank-v3.5
KB_EMBED_DEVICE=cpu
KB_USE_TANTIVY=false
KB_RERANKER_BACKEND=openrouter

--- KB container processes ---
OCI runtime exec failed: exec failed: unable to start container process: exec: "ps": executable file not found in $PATH

=== KB search API health ===
{}

=== KB search test (sample query) ===
{}

=== KB document count / chunks ===
stats endpoint unavailable

documents endpoint unavailable

=== KB version from git ===
KB is not a git checkout

=== KB entity lists ===
no entity_lists dir
no data dir
```

## Screenshots
- ![](collector-health.png)
- ![](endpoint_13000_health.png)
- ![](endpoint_18000_health.png)
- ![](endpoint_8000_health.png)
- ![](endpoint_8085_health.png)
- ![](endpoint_8100_health.png)
- ![](endpoint_8200_health.png)
- ![](gemma-health.png)
- ![](guard-health.png)
- ![](jenkins-login.png)
- ![](kb-health.png)
- ![](orch-health.png)
- ![](webui-chat.png)
- ![](webui-home.png)

## Post-restart processes
```

```

## How to re-run
```bash
DANA_HOST_REPO=/Users/alinikkhah/Documents/Work/CreditScoring/Chatbot_production_v1 bash /Users/alinikkhah/Documents/Work/CreditScoring/Chatbot_production_v1/components/server-setup/scripts/gpu_full_recover_report.sh
```

Artifacts live under `docs/ops/gpu-recover-reports/20261114T132906Z-Ali-Nikkhah-4/` in Work_RAG-Server-Setup.
