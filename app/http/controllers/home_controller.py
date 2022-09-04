from laraton.controller import Controller
from laraton.view import view
from app.models.user import User


class HomeController(Controller):

    def index(self, ):
        user = User.where('login', 'ololo').or_where('id', '>', '0').first()
        return view('home.index', {'a': user, 'b': 123})
