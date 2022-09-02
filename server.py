from laraton.router import Router
def process_http_request(environ, start_response):
    exec(open("routes/web.py").read())
    router = Router()
    text = router.run()

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = text.encode('utf-8')
    return [text]