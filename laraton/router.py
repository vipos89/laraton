from laraton.route import Route


class Router:
    routes = []

    def get(route: str, controller):
        Router.routes.append(Route(route, controller))
        pass

    def post():
        pass

    def put():
        pass

    def delete():
        pass

    def add_route():
        pass

    def run(self):
        route = Router.routes[0]
        controller, method = route.controller
        controller = controller()

        return getattr(controller, method)()