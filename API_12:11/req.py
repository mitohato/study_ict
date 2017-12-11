import json
import urllib.request

req = urllib.request.urlopen("http://localhost:8080")
res = req.read()
print(json.loads(res))
