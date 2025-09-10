from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class LoginScreen(Screen):
    usuario = StringProperty("")
    senha = StringProperty("")

    def do_login(self):
        if self.usuario == "admin" and self.senha == "123":
            self.manager.current = "home"
        else:
            print("Login inválido!")

    def forgot_password(self):
        print("Usuário clicou em 'Esqueci a senha'")

    def register(self):
        print("Usuário clicou em 'Registrar-se agora'")
