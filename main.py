

from kivy.app import App
from kivy.app import Builder

GUI =  Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return GUI

if __name__ == '__main__':
    MyApp().run()
