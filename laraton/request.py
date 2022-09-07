from urllib.parse import parse_qs


class Request:
    def __init__(self, environ):
        pass

    def __get_get_params(self, raw_url):
        self.GET = parse_qs(raw_url)

    def input(self):
        pass

    def get(self):
        pass

    def post(self):
        pass

    def all(self):
        pass
