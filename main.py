from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Window.size = (400, 300)

class FirstPage(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def login_info(self):
        
        self.ids.lbl_info.text = ''
        self.ids.lbl_info.text = "[color=#FF0000]username and/or password required[/color]"


    

class SecondPage(Screen):
    pass

class ForgotPassword(Screen):
    pass

class CreateAccount(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("app2.kv")
class Main(App):
    def build(self):
        return kv

if __name__ == '__main__':
    Main().run()
