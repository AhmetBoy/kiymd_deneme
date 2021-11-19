from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
Window.size = (300,500)
class Myt(BoxLayout):
    def __init__(self,**kwargs):
        super(Myt,self).__init__(**kwargs)



class deneme(MDApp):
    def build(self):
        return Myt()
deneme().run()