from laraton.router import Router
from app.http.controllers.home_controller import HomeController

Router.get('', [HomeController, 'index']).name('home')
Router.get('/test/{id}', [HomeController, 'test2'])
