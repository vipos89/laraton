from laraton.controller import Controller
from laraton.view import view
import sqlite3


class HomeController(Controller):

    def index(self):

        return view('home.index', {'a': 111, 'b': 123})
