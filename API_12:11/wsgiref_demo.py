from wsgiref.simple_server import make_server, demo_app

with make_server("", 8080, demo_app) as httpd:
    print("localhost:8080")

    httpd.serve_forever()
