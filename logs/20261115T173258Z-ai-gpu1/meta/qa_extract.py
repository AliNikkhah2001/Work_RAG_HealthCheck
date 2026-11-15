import sys, json, re
p = sys.argv[1]
try:
    raw = open(p, encoding="utf-8", errors="replace").read()
except Exception:
    print("Q\t"); print("A\t"); sys.exit(0)
q, a = "", ""
try:
    d = json.loads(raw)
    # WebUI E2E shape: {"signin":..,"model":..,"chat_http":..,"answer":..}
    if "answer" in d or "signin" in d:
        a = d.get("answer", "") or ""
        q = d.get("question", "") or ""
    else:
        q = (d.get("messages") or [{}])[0].get("content", "") or d.get("query", "")
        ch = d.get("choices") or []
        if ch:
            a = (ch[0].get("message") or {}).get("content", "") or (ch[0].get("delta") or {}).get("content", "")
except Exception:
    pass
if not a and "data:" in raw:
    parts = []
    for m in re.finditer(r'^data:\s*(\{.*\})\s*$', raw, re.M):
        try:
            obj = json.loads(m.group(1))
            for c in (obj.get("choices") or []):
                delta = c.get("delta") or {}
                if delta.get("content"):
                    parts.append(delta["content"])
                msg = c.get("message") or {}
                if msg.get("content"):
                    parts.append(msg["content"])
        except Exception:
            continue
    a = "".join(parts)
if not a:
    m = re.search(r'"content"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
    if m:
        a = m.group(1)
print("Q\t" + q.replace("\n", " "))
print("A\t" + a.replace("\n", " "))
