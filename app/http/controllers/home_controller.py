from laraton.controller import Controller
from laraton.view import view
from app.models.user import User


class HomeController(Controller):

    def index(self, id: int = 1):
        user = User.where('login', 'ololo').or_where('id', '>', '0').first()
        return view('home.index', {'a': user, 'b': 123})

    def test(self,  id:int = 1):
        user = User.where('login', 'ololo').or_where('id', '>', '0').first()
        return view('home.index', {'a': user, 'b': 2222222})

    def test2(self, id):
        return str(id)