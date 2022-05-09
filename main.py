from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
Builder.load_file("design.kv")
Window.size=(428,600)
class Login(Screen):
    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)



class AdminPage(Screen):
    def __init__(self,**kwargs):
        super(AdminPage,self).__init__(**kwargs)
        self.data = {
            "image-plus": "add photo",
        }
        
    def callback(self,instance):
        print('called from', instance.icon)


    def change_screen1(self):
        self.ids.scrn_mngr.current = 'V'
    def change_screen2(self):
        self.ids.scrn_mngr.current = 'M'
    def change_screen3(self):
        self.ids.scrn_mngr.current = 'MÜ'
    def change_screen4(self):
        pass
    def callback(self):
        print("geldi")


class UserPage(Screen):
    def __init__(self,**kwargs):
        super(UserPage,self).__init__(**kwargs)
    
    def b(self):
        a = self.ids.products
        mdcard = MDCard(padding=10)
        image = Image(source="youtube.png")
        mdcard.add_widget(image)
        a.add_widget(mdcard)



class UserPage2(Screen):
     data = {
        "language-python": "Python",
        "language-php": "PHP",
        "language-cpp": "C++",
    }
        


class ScreenManagement(ScreenManager):
    pass

class login(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        # self.theme_cls.primary_hue = "200"
        return ScreenManagement()
    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

login().run()