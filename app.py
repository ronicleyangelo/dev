from kivy.app import App
from core.router import Router


class EscolarFutebolApp(App):
    def build(self):
        self.title = "Escolar Futebol App"
        return Router().build()  # Retorna o ScreenManager
