# GPU Full Recovery Report — `20261114T165924Z-ai-gpu1`

| Field | Value |
|------|------|
| UTC | 2026-11-14T17:02:00Z |
| Host | ai-gpu1 |
| Status | **HEALTHY** |
| Mode | `compose` |
| Umbrella HEAD | c614c32 |
| last_good | 13188eddd14d22dfb976f54babe5dfa645b63a77 |
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
18000  gemma            000        
9000   manager          200        
8000   kb               200        
8200   guardrails       200        
8100   orchestrator     200        
3000   trace-collector  000        
3001   langfuse         000        
13000  webui            200        
8085   jenkins          200        
8010   service:8010     200        
8001   service:8001     200        
8002   service:8002     200        
8003   service:8003     200        
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
KB container: pgvector-kb-prod
--- KB container env ---
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin
POSTGRES_USER=postgres
POSTGRES_PASSWORD=REDACTED
POSTGRES_DB=kb_manager
PGDATA=/var/lib/postgresql/data

--- KB container processes ---
OCI runtime exec failed: exec failed: unable to start container process: exec: "ps": executable file not found in $PATH

=== KB search API health ===
{
    "status": "ok",
    "db_mode": "pgvector",
    "db_driver": "asyncpg",
    "db_url": "127.0.0.1:5432/kb_manager",
    "db_ok": true,
    "doc_count": 21,
    "chunk_count": 1319,
    "reranker_ok": true,
    "embed_backend": "local",
    "reranker_backend": "local",
    "reranker_model": "BAAI/bge-reranker-v2-m3",
    "reranker_error": null,
    "dense_ok": true,
    "llm_upstream_mode": "self_hosted",
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
            "content": "\u0633\u0648\u0627\u0644: \u0622\u06cc\u0627 \u0633\u0627\u0628\u0642\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0633\u0627\u0645\u0627\u0646\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0645\u0646 \u0627\u062b\u0631 \u0645\u06cc\u200c\u06af\u0630\u0627\u0631\u062f\u061f\n\u067e\u0627\u0633\u062e \u06a9\u0648\u062a\u0627\u0647: \u062e\u06cc\u0631. \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f.\n\u067e\u0627\u0633\u062e \u06a9\u0627\u0645\u0644: \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f. \u0633\u0627\u0628\u0642\u0647 \u062a\u0633\u0647\u06cc\u0644\u0627\u062a (\u0686\u0647 \u0645\u0633\u062a\u0642\u06cc\u0645 \u0648 \u0686\u0647 \u062f\u0631 \u0646\u0642\u0634 \u0636\u0627\u0645\u0646)\u060c \u0686\u06a9\u200c\u0647\u0627\u06cc \u0628\u0631\u06af\u0634\u062a\u06cc\u060c \u0628\u062f\u0647\u06cc\u200c\u0647\u0627\u06cc \u0645\u0627\u0644\u06cc\u0627\u062a\u06cc\u060c \u0645\u062d\u06a9\u0648\u0645\u06cc\u062a \u0645\u0627\u0644\u06cc \u0648 \u0642\u0636\u0627\u06cc\u06cc \u0648 \u0635\u062f\u06a9 \u062f\u0631\u0622\u0645\u062f\u06cc \u062f\u0631 \u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u062f\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0627\u0639\u062a\u0628\u0627\u0631\u06cc \u0627\u0641\u0631\u0627\u062f \u062a\u0627\u062b\u06cc\u0631\u06af\u0630\u0627\u0631 \u0627\u0633\u062a.\n\u062f\u0633\u062a\u0647\u200c\u0628\u0646\u062f\u06cc: \u0639\u0648\u0627\u0645\u0644 \u0645\u0648\u062b\u0631 \u0628\u0631 \u0627\u0645\u062a\u06cc\u0627\u0632",
            "bm25_score": 76.9812,
            "semantic_score": 0.0,
            "dense_score": 0.0,
            "hybrid_score": 0.0,
            "rerank_score": 0.0,
            "ordinal": 263
        },
        {
            "chunk_id": "cb143421-5868-4723-bb14-a92671cb3deb",
            "doc_id": "7468c636-f116-4967-be6e-41671e960eb7",
            "doc_title": "\u0628\u0627\u0646\u06a9 \u0633\u0648\u0627\u0644\u0627\u062a \u0627\u0641\u0631\u0627\u062f \u062f\u0631 \u0632\u0645\u06cc\u0646\u0647 \u06af\u0632\u0627\u0631\u0634 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062a\u0633\u0647\u06cc\u0644\u0627\u062a-\u0627\u0635\u0644\u06cc",
            "heading_path": "Sheet: Sheet1",
            "folder_hierarchy": [
                "\u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u0646\u0634",
                "\u0627\u0634\u062e\u0627\u0635 \u062d\u0642\u06cc\u0642\u06cc",
                "\u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062a\u0633\u0647\u06cc\u0644\u0627\u062a",
                "\u0628\u0627\u0646\u06a9 \u0633\u0648\u0627\u0644\u0627\u062a"
            ],
            "content_preview": "\u0633\u0648\u0627\u0644: \u0622\u06cc\u0627 \u0633\u0627\u0628\u0642\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0633\u0627\u0645\u0627\u0646\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0645\u0646 \u0627\u062b\u0631 \u0645\u06cc\u200c\u06af\u0630\u0627\u0631\u062f\u061f\n\u067e\u0627\u0633\u062e \u06a9\u0648\u062a\u0627\u0647: \u062e\u06cc\u0631. \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f.\n\u067e\u0627\u0633\u062e \u06a9\u0627\u0645\u0644: \u062e\u06cc\u0631. \u062f\u0631 \u062d\u0627\u0644 \u062d\u0627\u0636\u0631 \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u0645\u0631\u0628\u0648\u0637 \u0628\u0647 \u0633\u0641\u062a\u0647 \u062f\u0631 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u0627\u0641\u0631\u0627\u062f \u0648 \u0634\u0631\u06a9\u062a \u0647\u0627 \u0644\u062d\u0627\u0638 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f. \u0633\u0627\u0628\u0642\u0647 \u062a\u0633\u0647\u06cc\u0644\u0627\u062a (\u0686\u0647 \u0645\u0633\u062a\u0642\u06cc\u0645 \u0648 \u0686\u0647 \u062f\u0631 \u0646\u0642\u0634 \u0636\u0627\u0645\u0646) \u060c \u0686\u06a9\u200c\u0647\u0627\u06cc \u0628\u0631\u06af\u0634\u062a\u06cc\u060c \u0628\u062f\u0647\u06cc\u200c\u0647\u0627\u06cc \u0645\u0627\u0644\u06cc\u0627\u062a\u06cc\u060c \u0645\u062d\u06a9\u0648\u0645\u06cc\u062a \u0645\u0627\u0644\u06cc \u0648 \u0642\u0636\u0627\u06cc\u06cc \u0648 \u0635\u062f\u06a9 \u062f\u0631\u0622\u0645\u062f\u06cc \u062f\u0631 \u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u062f\u0647 \u0627\u0639\u062a\u0628\u0627\u0631\u0633\u0646\u062c\u06cc \u062b\u0628\u062a \u0645\u06cc\u200c\u0634\u0648\u062f \u0648 \u0628\u0631 \u0631\u062a\u0628\u0647 \u0648 \u0627\u0645\u062a\u06cc\u0627\u0632 \u0627\u0639\u062a\u0628\u0627\u0631\u06cc \u0627\u0641\u0631\u0627\u062f \u062a\u0627\u062b\u06cc\u0631\u06af\u0630\u0627\u0631 \u0627\u0633\u062a.\n\u062f\u0633\u062a\u0647\u200c\u0628\u0646\u062f\u06cc: \u0633\u0648\u0627\u0628\u0642 \u0645\u0646\u0641\u06cc \u0648 \u0628\u062f\u0647\u06cc\u200c\u0647\u0627",
```

## Screenshots
_none_

## Post-restart processes
```
root      744790  2.6  0.0 596596 132448 ?       Rl   Nov12  94:14 offline-prep/venv/bin/python -m uvicorn llm_inference_manager.app:app --host 0.0.0.0 --port 9000 --app-dir /splunk-data/v1/Work_RAG-Server-Setup
root      878415  0.2  0.0 187048 84892 ?        Sl   Nov12   8:13 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn work_rag_guardrails.api:create_app --factory --host 0.0.0.0 --port 8200
root     1053481  1.0  0.0 3480292 432648 ?      Ssl  Nov12  34:53 /usr/local/bin/python3 -m uvicorn open_webui.main:app --host 0.0.0.0 --port 8080 --forwarded-allow-ips * --workers 1 --ws-per-message-deflate true
999      1062294  0.0  0.0 17247808 409524 ?     Ss   Nov12   0:11 postgres
999      1062410  0.0  0.0 17247940 192908 ?     Ss   Nov12   0:00 postgres: checkpointer 
999      1062411  0.0  0.0 17247964 192324 ?     Ss   Nov12   0:02 postgres: background writer 
999      1062413  0.0  0.0 17247808 77476 ?      Ss   Nov12   0:02 postgres: walwriter 
999      1062414  0.0  0.0 17249404 62136 ?      Ss   Nov12   0:03 postgres: autovacuum launcher 
999      1062415  0.0  0.0 17249392 61620 ?      Ss   Nov12   0:00 postgres: logical replication launcher 
root     1070192  0.3  0.3 41248180 3664460 ?    Sl   Nov12  11:50 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn kb_manager.web.app:app --host 0.0.0.0 --port 8000
999      1070246  0.0  0.0 17251772 110572 ?     Ss   Nov12   0:04 postgres: postgres kb_manager 172.17.0.1(50366) idle
root     1072136  0.3  0.1 30335700 2010480 ?    Sl   Nov12  11:48 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn work_rag_orchestrator.api:create_app --factory --host 0.0.0.0 --port 8100
root     1848116  0.6  0.0  59280 50744 ?        Ss   16:59   0:00 python -m uvicorn app:app --host 0.0.0.0 --port 3000
999      1848117  0.0  0.0 220368 29952 ?        Ss   16:59   0:00 postgres
999      1848553  0.0  0.0 220500  6216 ?        Ss   16:59   0:00 postgres: checkpointer 
999      1848554  0.0  0.0 220524  7364 ?        Ss   16:59   0:00 postgres: background writer 
999      1848556  0.0  0.0 220368 10356 ?        Ss   16:59   0:00 postgres: walwriter 
999      1848557  0.0  0.0 221964  9360 ?        Ss   16:59   0:00 postgres: autovacuum launcher 
999      1848558  0.0  0.0 221952  8448 ?        Ss   16:59   0:00 postgres: logical replication launcher 
root     1856205  0.0  0.0   2572  1384 ?        Ss   17:01   0:00 /usr/bin/tini -- /usr/local/bin/jenkins.sh
root     1856371 61.9  0.0 43733136 427220 ?     Sl   17:01   0:18 java -Duser.home=/var/jenkins_home -Djenkins.install.runSetupWizard=false -Djenkins.model.Jenkins.slaveAgentPort=50000 -Dhudson.lifecycle=hudson.lifecycle.ExitLifecycle -jar /usr/share/jenkins/jenkins.war
```

## How to re-run
```bash
DANA_HOST_REPO=/splunk-data/production/Work_Credit-RAG_Phase1 bash /splunk-data/production/Work_Credit-RAG_Phase1/components/server-setup/scripts/gpu_full_recover_report.sh
```

Artifacts live under `docs/ops/gpu-recover-reports/20261114T165924Z-ai-gpu1/` in Work_RAG-Server-Setup.
