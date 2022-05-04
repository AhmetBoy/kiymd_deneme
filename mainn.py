from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker, MapMarkerPopup
class Login(Screen):
    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)



class AdminPage(Screen):
    def change_screen1(self):
        self.ids.scrn_mngr.current = 'V'
    def change_screen2(self):
        self.ids.scrn_mngr.current = 'M'
    def change_screen3(self):
        self.ids.scrn_mngr.current = 'MÜ'
    def change_screen4(self):
        self.ids.scrn_mngr.current = 'L'

class UserPage(Screen):
    def __init__(self,**kwargs):
        super(UserPage,self).__init__(**kwargs)

    
    def change_screen1(self):
        self.ids.scrn_mngr.current = 'V'
    def change_screen2(self):
        self.ids.scrn_mngr.current = 'M'
    def change_screen3(self):
        self.ids.scrn_mngr.current = 'MÜ'
    def change_screen4(self):
        self.ids.scrn_mngr.current = 'L'



class ScreenManagement(ScreenManager):
    pass

class loginn(MDApp):
    def build(self):
        return ScreenManagement()

loginn().run()