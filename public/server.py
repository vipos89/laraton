import sys

sys.path.append('..')

import os
from dotenv import load_dotenv
from laraton.router import Router



def process_http_request(environ, start_response):
    os.environ['APP_PATH'] = os.path.join(os.path.abspath(os.curdir), '..')
    env_path = os.path.join(os.getenv('APP_PATH'), '.env')

    load_dotenv(dotenv_path=env_path)

    exec(open(os.path.join(os.getenv('APP_PATH'), 'routes', 'web.py')).read())
    router = Router()
    text = router.run()

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = text.encode('utf-8')
    return [text]


