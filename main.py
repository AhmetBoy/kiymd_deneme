from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineListItem
class A(BoxLayout):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class main(MDApp):
    def build(self):
        return A()
main().run()
