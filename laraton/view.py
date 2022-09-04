import os
from jinja2 import Template
from types import SimpleNamespace


def view(template: str = '', data: dict = {}):
    path = os.path.join(os.getenv('APP_PATH'), 'views', *template.split('.')) + '.html'
    if os.path.exists(path):
        html = open(path).read()
        template = Template(html)
        return template.render(data)
    else:
        return 'not found'
