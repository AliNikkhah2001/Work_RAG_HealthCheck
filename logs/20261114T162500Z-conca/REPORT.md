# GPU Full Recovery Report — `20261114T153737Z-Ali-Nikkhah-4`

| Field | Value |
|------|------|
| UTC | 2026-11-14T15:38:44Z |
| Host | Ali-Nikkhah-4.local |
| Status | **HEALTHY** |
| Mode | `compose` |
| Umbrella HEAD | 7cd59c7 |
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
chat_webui http=200
kb_search http=200
qa_pass=3/3
```

## Knowledgebase details
```
=== Knowledgebase container ===
KB container: dana-local-kb-1
--- KB container env ---
KB_DB_MODE=pgvector
KB_EMBED_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
KB_EMBED_BACKEND=local
KB_REDIS_URL=redis://REDACTED
KB_RERANKER_MODEL=cohere/rerank-v3.5
KB_OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
KB_EMBED_DIM=384
KB_RERANKER_DEVICE=cpu
KB_DB_URL=postgresql://REDACTED
KB_OPENROUTER_API_KEY=REDACTED
KB_USE_TANTIVY=false
KB_WEB_PORT=8000
KB_EMBED_DEVICE=cpu
KB_RERANKER_BACKEND=openrouter
KB_WEB_HOST=0.0.0.0
HF_HOME=/models
HF_HUB_CACHE=/models

--- KB container processes ---
OCI runtime exec failed: exec failed: unable to start container process: exec: "ps": executable file not found in $PATH

=== KB search API health ===
{
    "status": "ok",
    "db_mode": "pgvector",
    "db_driver": "asyncpg",
    "db_url": "postgres:5432/kb_manager",
    "db_ok": true,
    "doc_count": 21,
    "chunk_count": 1319,
    "reranker_ok": true,
    "embed_backend": "local",
    "reranker_backend": "openrouter",
    "reranker_model": "cohere/rerank-v3.5",
    "reranker_error": null,
    "dense_ok": true,
    "llm_upstream_mode": "openrouter",
    "error": null
}

=== KB search test (sample query) ===
{
    "query": "\u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc",
    "normalized_query": "\u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc",
    "tokens": [
        "\u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc",
        "\u0627\u0639\u062a",
        "\u0639\u062a\u0628",
        "\u062a\u0628\u0627",
        "\u0628\u0627\u0631",
        "\u0627\u0631\u0633",
        "\u0631\u0633\u0646",
        "\u0633\u0646\u062c",
        "\u0646\u062c\u06cc"
    ],
    "total_chunks_indexed": 1298,
    "bm25_results": [
        {
            "chunk_id": "74b21260-ee67-4006-aef3-a9b07cf38e08",
            "doc_id": "706eff4e-e9ba-4f4a-8fda-f1f358a8e3de",
            "doc_title": "\u0628\u0627\u0646\u06a9 \u0633\u0648\u0627\u0644\u0627\u062a \u0627\u0641\u0631\u0627\u062f \u062f\u0631 \u0632\u0645\u06cc\u0646\u0647 \u06af\u0632\u0627\u0631\u0634 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062a\u0633\u0647\u06cc\u0644\u0627\u062a",
            "heading_path": "Sheet: \u0633\u0648\u0627\u0644\u0627\u062a \u062d\u0642\u0648\u0642\u06cc",
            "folder_hierarchy": [
                "\u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u0646\u0634",
                "\u0627\u0634\u062e\u0627\u0635 \u062d\u0642\u0648\u0642\u06cc",
                "\u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062a\u0633\u0647\u06cc\u0644\u0627\u062a",
                "\u0628\u0627\u0646\u06a9 \u0633\u0648\u0627\u0644\u0627\u062a \u0627\u0641\u0631\u0627\u062f \u062f\u0631 \u0632\u0645\u06cc\u0646\u0647 \u06af\u0632\u0627\u0631\u0634 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062a\u0633\u0647\u06cc\u0644\u0627\u062a"
            ],
            "content_preview": "\u0633\u0648\u0627\u0644: \u0622\u06cc\u0627 \u0633\u0627\u0628\u0642\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0633\u0627\u0645\u0627\u0646\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0645\u0646 \u0627\u062b\u0631 \u0645\u06cc\u200c\u06af\u0630\u0627\u0631\u062f\u061f\n\u067e\u0627\u0633\u062e \u06a9\u0648\u062a\u0627\u0647: \u062e\u06cc\u0631. \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f.\n\u067e\u0627\u0633\u062e \u06a9\u0627\u0645\u0644: \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f. \u0633\u0627\u0628\u0642\u0647 \u062a\u0633\u0647\u06cc\u0644\u0627\u062a (\u0686\u0647 \u0645\u0633\u062a\u0642\u06cc\u0645 \u0648 \u0686\u0647 \u062f\u0631 \u0646\u0642\u0634 \u0636\u0627\u0645\u0646)\u060c \u0686\u06a9\u200c\u0647\u0627\u06cc \u0628\u0631\u06af\u0634\u062a\u06cc\u060c \u0628\u062f\u0647\u06cc\u200c\u0647\u0627\u06cc \u0645\u0627\u0644\u06cc\u0627\u062a\u06cc\u060c \u0645\u062d\u06a9\u0648\u0645\u06cc\u062a \u0645\u0627\u0644\u06cc \u0648 \u0642\u0636\u0627\u06cc\u06cc \u0648 \u0635\u062f\u06a9 \u062f\u0631\u0622\u0645\u062f\u06cc \u062f\u0631 \u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u062f\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0627\u0639\u062a\u0628\u0627\u0631\u06cc \u0627\u0641\u0631\u0627\u062f \u062a\u0627\u062b\u06cc\u0631\u06af\u0630\u0627\u0631 \u0627\u0633\u062a.\n\u062f\u0633\u062a\u0647\u200c\u0628\u0646\u062f\u06cc: \u0639\u0648\u0627\u0645\u0644 \u0645\u0648\u062b\u0631 \u0628\u0631 \u0627\u0645\u062a\u06cc\u0627\u0632",
            "bm25_score": 79.6946,
            "semantic_score": 0.0,
            "dense_score": 0.0,
            "hybrid_score": 0.0,
            "rerank_score": 0.0,
            "ordinal": 263
        },
        {
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
no restart data
```

## How to re-run
```bash
DANA_HOST_REPO=/Users/alinikkhah/Documents/Work/CreditScoring/chatbot-health-dashboard bash /Users/alinikkhah/Documents/Work/CreditScoring/chatbot-health-dashboard/components/server-setup/scripts/gpu_full_recover_report.sh
```

Artifacts live under `docs/ops/gpu-recover-reports/20261114T153737Z-Ali-Nikkhah-4/` in Work_RAG-Server-Setup.
