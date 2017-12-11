from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text_plain; charset=utf-8')]
    start_response(status, headers)

    return [b'Hello World']

with make_server("", 8080, app) as httpd:
    print("localhost:8080")
    httpd.serve_forever()
