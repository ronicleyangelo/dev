from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def on_enter(self):
        print("Entrou na HomeScreen")
