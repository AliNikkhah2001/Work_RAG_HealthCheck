import html
import json
import re
import sys
from pathlib import Path

e2e = Path(sys.argv[1])
out_parts: list[str] = []


def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def item(name: str, question: str, answer: str, code: str, *, note: str = "") -> str:
    ok = code == "200"
    status = "PASS" if ok else "FAIL"
    cls = "status-passed" if ok else "status-failed"
    q_html = f'<div class="qa-question">❓ {esc(question)}</div>' if question else ""
    if answer:
        a_html = f'<div class="qa-answer">🤖 {esc(answer)}</div>'
    elif ok and not answer:
        a_html = (
            '<div class="qa-answer" style="color:#888;">'
            "(HTTP 200 but answer text missing in artifact — check e2e/random_qa.json)"
            "</div>"
        )
    else:
        a_html = (
            '<div class="qa-answer" style="color:#888;">'
            "(no answer captured — request failed or service unreachable)"
            "</div>"
        )
    extra = f'<div class="qa-status">{esc(note)}</div>' if note else ""
    return (
        f'<div class="qa-item"><h4>{esc(name)}</h4>{q_html}{a_html}'
        f'<div class="qa-status">HTTP: {esc(code or "—")} — '
        f'<span class="{cls}">{status}</span></div>{extra}</div>'
    )


def extract_legacy(path: Path) -> tuple[str, str]:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "", ""
    q = a = ""
    try:
        d = json.loads(raw)
        if "answer" in d or "signin" in d:
            a = d.get("answer", "") or ""
            q = d.get("question", "") or ""
        else:
            q = (d.get("messages") or [{}])[0].get("content", "") or d.get("query", "")
            ch = d.get("choices") or []
            if ch:
                a = (ch[0].get("message") or {}).get("content", "") or (
                    ch[0].get("delta") or {}
                ).get("content", "")
    except Exception:
        pass
    if not a and "data:" in raw:
        parts = []
        for m in re.finditer(r"^data:\s*(\{.*\})\s*$", raw, re.M):
            try:
                obj = json.loads(m.group(1))
                for c in obj.get("choices") or []:
                    delta = c.get("delta") or {}
                    if delta.get("content"):
                        parts.append(delta["content"])
                    msg = c.get("message") or {}
                    if msg.get("content"):
                        parts.append(msg["content"])
            except Exception:
                continue
        a = "".join(parts)
    return q, a


random_qa = e2e / "random_qa.json"
if random_qa.is_file():
    try:
        data = json.loads(random_qa.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    results = data.get("results") if isinstance(data, dict) else None
    if isinstance(results, list) and results:
        for i, row in enumerate(results, 1):
            if not isinstance(row, dict):
                continue
            gen = row.get("generation") or {}
            ret = row.get("retrieval") or {}
            q = row.get("question") or ""
            a = gen.get("answer_preview") or gen.get("answer") or ""
            code = str(gen.get("http") or ("200" if row.get("passed") else "000"))
            note = (
                f"retrieval_http={ret.get('http')} hits={ret.get('hits')} "
                f"chunks_used={gen.get('chunks_used')} wall_ms={row.get('e2e_wall_ms')}"
            )
            out_parts.append(item(f"random_qa_{i}", q, a, code, note=note))
        seed = data.get("seed")
        n = data.get("n")
        out_parts.append(
            item(
                "random_qa_batch",
                f"batch seed={seed} n={n}",
                f"See random_qa.json for full payloads ({len(results)} samples).",
                "200" if all((r or {}).get("passed") for r in results if isinstance(r, dict)) else "000",
            )
        )

# Legacy / additional summary rows (skip random_qa_* already rendered above)
summary = e2e / "summary.txt"
if summary.is_file():
    fallbacks = {
        "chat_greeting": "سلام",
        "chat_credit_qa": "اعتبارسنجی چیست؟",
        "chat_webui": "سلام، آیا سرویس فعال است؟",
        "kb_search": "اعتبارسنجی چیست (KB search)",
    }
    for line in summary.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name = line.split(" ", 1)[0]
        if name.startswith("random_qa"):
            continue
        code = ""
        m = re.search(r"http=(\d+)", line)
        if m:
            code = m.group(1)
        qfile = e2e / f"{name}.json"
        q, a = extract_legacy(qfile) if qfile.is_file() else ("", "")
        if not q:
            q = fallbacks.get(name, "")
        out_parts.append(item(name, q, a, code))

if not out_parts:
    print('<div style="color:#666;">No QA tests were run (services may be down).</div>')
else:
    print("".join(out_parts))
