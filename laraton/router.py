import re
from laraton.route import Route
from typing import Type


class Router:
    routes = []

    @classmethod
    def get(cls, pattern: str, controller, *args) -> Type[Route]:
        route = Route(pattern, controller, 'get')
        Router.routes.append(route)
        return route

    # def post():
    #     pass
    #
    # def put():
    #     pass
    #
    # def delete():
    #     pass
    #
    # def add_route():
    #     pass

    def run(self, request_method: str, url_string: str):
        for route in Router.routes:
            if route.method != request_method.lower():
                continue
            route_pattern = route.pattern
            route_pattern = route_pattern.replace('{', '(?P<')
            route_pattern = route_pattern.replace('}', '>\w+)')
            if len(url_string) > 0 and url_string[-1] == '/':
                url_string = url_string[:-1]

            pattern = f'^{route_pattern}$'
            match = re.match(pattern, url_string)
            if match is not None:
                res = match.groupdict()
                controller, method = route.controller


        #route = Router.routes[0]
        controller, method = route.controller
        controller = controller()

        return getattr(controller, method)()
