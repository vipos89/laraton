import re
import inspect
from laraton.route import Route
from typing import Type
from laraton.di.container import Container




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
            di_container = Container()
            route_pattern = route.pattern
            route_pattern = route_pattern.replace('{', '(?P<')
            route_pattern = route_pattern.replace('}', '>\w+)')
            if len(url_string) > 0 and url_string[-1] == '/':
                url_string = url_string[:-1]

            pattern = f'^{route_pattern}$'
            match = re.match(pattern, url_string)

            controller, method = None, None
            if match is not None:
                res = match.groupdict()
                controller, method = route.controller
                print(controller, method )
                constructor_args = di_container.resolve(controller)
                del constructor_args['self']
                controller_obj = controller(*constructor_args.values())
                method_to_call = getattr(controller_obj, method)
                methods_entries = di_container.get_entries(inspect.signature(method_to_call).parameters, controller_obj)
                attrs = methods_entries | res
                return method_to_call(*attrs.values())

              


        return getattr(controller, method)()
