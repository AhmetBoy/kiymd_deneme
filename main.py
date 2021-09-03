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
    # def on_start(self):
    #     for i in range(20):
    #         self.root.ids.container.add_widget(OneLineListItem(text=f"Single-line item {i}"))
main().run()