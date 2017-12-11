import json
from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'Application/json; charset=utf-8')]
    start_response(status, headers)

    with open("hoge.json", "r") as f:
        f = json.load(f)

        return [json.dumps(f).encode()]

with make_server("", 8080, app) as httpd:
     print("localhost:8080")
     httpd.serve_forever()
