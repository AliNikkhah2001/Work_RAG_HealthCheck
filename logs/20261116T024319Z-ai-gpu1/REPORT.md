# GPU Full Recovery Report — `20261116T024319Z-ai-gpu1`

| Field | Value |
|------|------|
| UTC | 2026-11-16T02:59:16Z |
| Host | ai-gpu1 |
| Status | **HEALTHY** |
| Mode | `compose` |
| Umbrella HEAD | 0663e2a |
| last_good | 7a504d48ae6d7a88a8ee343108f8427a2fad9c53 |
| deployed | none |
| QA | 10 / 10 chat passes |
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
9000   manager          200        
8000   kb               200        
8200   guardrails       200        
8100   orchestrator     200        
3000   trace-collector  000        
3001   langfuse         000        
13000  webui            200        
8085   jenkins          200        
8088   service:8088     200        
8010   service:8010     200        
8001   service:8001     200        
8002   service:8002     200        
8003   service:8003     200        
18000  gemma            200        
18100  service:18100    200        
18200  service:18200    200        
13100  service:13100    200        
```

## E2E summary
```
random_qa_1 http=200
random_qa_2 http=200
random_qa_3 http=200
random_qa_4 http=200
random_qa_5 http=200
random_qa_6 http=200
random_qa_7 http=200
random_qa_8 http=200
random_qa_9 http=200
random_qa_10 http=200
random_qa_batch passed=10/10 seed=1794797041
qa_pass=10/10
```

## Knowledgebase details
```
=== Knowledgebase container ===
KB container: dana-stage-kb-1
--- KB container env ---
KB_EMBED_BACKEND=local
KB_EMBED_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
KB_RERANKER_BACKEND=openrouter
HF_HUB_CACHE=/models
KB_DB_MODE=pgvector
KB_USE_TANTIVY=false
KB_WEB_HOST=0.0.0.0
KB_EMBED_DIM=384
HF_HOME=/models
KB_OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
KB_REDIS_URL=redis://REDACTED
KB_RERANKER_DEVICE=cpu
KB_OPENROUTER_API_KEY=
KB_DB_URL=postgresql://REDACTED
KB_WEB_PORT=8000
KB_EMBED_DEVICE=cpu
KB_RERANKER_MODEL=cohere/rerank-v3.5

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
```

## Screenshots
- ![](gemma-docs.png)
- ![](guard-docs.png)
- ![](jenkins-login.png)
- ![](jenkins-status.png)
- ![](kb-manager-docs.png)
- ![](kb-manager-redoc.png)
- ![](manager-docs.png)
- ![](manager-ui.png)
- ![](orch-docs.png)
- ![](webui-alt.png)
- ![](webui-main.png)
- ![](webui-stage.png)

## Post-restart processes
```
root      744790  2.6  0.0 596716 135100 ?       Sl   Nov12 148:20 offline-prep/venv/bin/python -m uvicorn llm_inference_manager.app:app --host 0.0.0.0 --port 9000 --app-dir /splunk-data/v1/Work_RAG-Server-Setup
root      878415  0.2  0.0 190436 88552 ?        Sl   Nov12  15:00 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn work_rag_guardrails.api:create_app --factory --host 0.0.0.0 --port 8200
999      1062294  0.0  0.0 17247808 409524 ?     Ss   Nov12   0:18 postgres
999      1062410  0.0  0.0 17247940 192908 ?     Ss   Nov12   0:00 postgres: checkpointer 
999      1062411  0.0  0.0 17247964 192324 ?     Ss   Nov12   0:04 postgres: background writer 
999      1062413  0.0  0.0 17247808 77476 ?      Ss   Nov12   0:04 postgres: walwriter 
999      1062414  0.0  0.0 17249404 62152 ?      Ss   Nov12   0:05 postgres: autovacuum launcher 
999      1062415  0.0  0.0 17249392 61620 ?      Ss   Nov12   0:00 postgres: logical replication launcher 
root     1070192  0.3  0.3 41268072 3688568 ?    Sl   Nov12  20:42 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn kb_manager.web.app:app --host 0.0.0.0 --port 8000
999      1070246  0.0  0.0 17251772 110608 ?     Ss   Nov12   0:12 postgres: postgres kb_manager 172.17.0.1(50366) idle
root     1072136  0.6  0.1 30503404 2043760 ?    Sl   Nov12  32:45 /splunk-data/v1/Work_RAG-Server-Setup/offline-prep/venv/bin/python -m uvicorn work_rag_orchestrator.api:create_app --factory --host 0.0.0.0 --port 8100
root     2592594  0.2  0.0  59280 51176 ?        Ss   Nov15   2:21 python -m uvicorn app:app --host 0.0.0.0 --port 3000
999      2592601  0.0  0.0 220368 29444 ?        Ss   Nov15   0:17 postgres
999      2592911  0.0  0.0 220500  9056 ?        Ss   Nov15   0:00 postgres: checkpointer 
999      2592912  0.0  0.0 220524  7316 ?        Ss   Nov15   0:00 postgres: background writer 
999      2592914  0.0  0.0 220368 10340 ?        Ss   Nov15   0:00 postgres: walwriter 
999      2592915  0.0  0.0 221964  9180 ?        Ss   Nov15   0:01 postgres: autovacuum launcher 
999      2592916  0.0  0.0 221952  8520 ?        Ss   Nov15   0:00 postgres: logical replication launcher 
999      2594965  0.0  0.0 225736 20236 ?        Ss   Nov15   0:03 postgres: postgres kb_manager 172.30.101.6(44616) idle
root     2597304  0.9  0.0 3611380 373292 ?      Ssl  Nov15   7:35 /usr/local/bin/python3 -m uvicorn open_webui.main:app --host 0.0.0.0 --port 8080 --forwarded-allow-ips * --workers 1 --ws-per-message-deflate true
root     2767588  0.0  0.0   2564  1492 ?        Ss   Nov15   0:02 /usr/bin/tini -- /usr/local/bin/jenkins.sh
root     2767738  0.8  0.1 42866384 1220048 ?    Sl   Nov15   5:55 java -Duser.home=/var/jenkins_home -Djenkins.install.runSetupWizard=false -Djenkins.model.Jenkins.slaveAgentPort=50000 -Dhudson.lifecycle=hudson.lifecycle.ExitLifecycle -jar /usr/share/jenkins/jenkins.war
root     2806424  1.2  0.0 3145608 360104 ?      Ssl  Nov15   8:43 /usr/local/bin/python3 -m uvicorn open_webui.main:app --host 0.0.0.0 --port 8080 --forwarded-allow-ips * --workers 1 --ws-per-message-deflate true
999      2867876  0.0  0.0 17251660 63868 ?      Ss   Nov15   0:03 postgres: postgres kb_manager 172.17.0.1(53914) idle
```

## How to re-run
```bash
DANA_HOST_REPO=/splunk-data/production/Work_Credit-RAG_Phase1 bash /splunk-data/production/Work_Credit-RAG_Phase1/components/server-setup/scripts/gpu_full_recover_report.sh
```

Artifacts live under `docs/ops/gpu-recover-reports/20261116T024319Z-ai-gpu1/` in Work_RAG-Server-Setup.
