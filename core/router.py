from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen


class Router:
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        return sm
