import sys, json, urllib.request, urllib.error
base = sys.argv[1].rstrip("/")
email = sys.argv[2] if len(sys.argv) > 2 else "admin@localhost"
password = sys.argv[3] if len(sys.argv) > 3 else "admin"
question = sys.argv[4] if len(sys.argv) > 4 else "اعتبارسنجی چیست؟"

def call(path, data=None, token=None, timeout=120):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(base + path, data=body, headers=headers)
    return urllib.request.urlopen(req, timeout=timeout)

res = {"signin": "none", "model": "", "chat_http": 0, "answer": "", "error": ""}
token = ""
# 1) sign in
try:
    d = json.loads(call("/api/v1/auths/signin", {"email": email, "password": password}).read().decode())
    token = d.get("token", "")
    res["signin"] = "ok" if token else "no-token"
except urllib.error.HTTPError as e:
    res["signin"] = "http-%d" % e.code
except Exception as e:
    res["signin"] = "err"
    res["error"] = str(e)[:200]
# 2) discover served model
model = ""
try:
    d = json.loads(call("/api/models", token=token, timeout=30).read().decode())
    ids = [m.get("id") for m in (d.get("data") or []) if m.get("id")]
    if ids:
        model = ids[0]
except Exception:
    pass
if not model:
    model = "ics-helper-agent"
res["model"] = model
# 3) chat
try:
    raw = call("/api/chat/completions",
               {"model": model, "messages": [{"role": "user", "content": question}], "stream": False},
               token=token).read().decode()
    res["chat_http"] = 200
    try:
        d = json.loads(raw)
        res["answer"] = ((d.get("choices") or [{}])[0].get("message") or {}).get("content", "") or raw[:2000]
    except Exception:
        res["answer"] = raw[:2000]
except urllib.error.HTTPError as e:
    res["chat_http"] = e.code
    res["error"] = e.read().decode(errors="replace")[:300]
except Exception as e:
    res["error"] = str(e)[:300]
print(json.dumps(res, ensure_ascii=False))
