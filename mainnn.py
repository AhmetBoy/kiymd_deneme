from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFillRoundFlatIconButton
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
import urllib.request,requests
import urllib.request, re, webbrowser, os
from pytube import YouTube

Builder.load_file("design.kv")
Window.size=(700,600)
class Login(Screen):
    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)



class Download(Screen):
    def __init__(self,**kwargs):
        super(Download,self).__init__(**kwargs)
        self.data = {
            "image-plus": "add photo",
        }
        self.store = Store()

    def make_search_id(self):
        searched_word = self.ids.search_word.text
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searched_word)
        self.video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        self.send()
    def send(self):
        image_name_list = []
        self.url_list = []
        id_index = 0
        for i in self.video_ids:  
            video_link = "https://www.youtube.com/watch?v=" + i
            self.url_list.append(video_link)
            image_name = str(i) + ".jpg"
            yt = YouTube(video_link)
            author = yt.author
            title = yt.title
            date = yt.publish_date
            try:
                thumbnail_url = "https://img.youtube.com/vi/"+str(i)+"/maxresdefault.jpg"
                urllib.request.urlretrieve(thumbnail_url , image_name)
            except:
                urllib.request.urlretrieve(yt.thumbnail_url , image_name)
            image_name_list.append(image_name)
            self.creat_blog(title, author, date, image_name, id_index)
            id_index += 1
            if id_index == 3:
                self.delete_image(image_name_list)
                break
    
    def delete_image(self, image_name_list):
        for i in (image_name_list):
            try:os.remove(str(i))
            except:pass

    def creat_blog(self, title, author, date, image_name, id_index):
        gridLayout = self.ids.grd_downloadPage
        mdCard = MDCard(spacing=10, padding=[10,10], radius=[10], elevation=15)
        box1 = BoxLayout(size_hint_x=.4)
        deneme_card = MDCard(radius=[10])
        image = Image(source=str(image_name))
        box2 = BoxLayout(orientation="vertical", size_hint_x=.6)
        box3 = BoxLayout(orientation="vertical", pos_hint={"center_x":.5, "center_y":.9}, size_hint_y=.6)
        mdLabel1 = MDLabel(text=str(title))
        mdLabel2 = MDLabel(text=str(author))
        mdLabel3 = MDLabel(text=str(date))
        box4 = BoxLayout(spacing=4)
        mdIconButton1 = MDFillRoundFlatIconButton(on_press=lambda x:self.download_mp3(id_index), text="MP3", icon="youtube",user_font_size="48sp")
        mdIconButton2 = MDFillRoundFlatIconButton(on_press=lambda x:self.download_mp4(id_index), text="MP4", icon="youtube",user_font_size="48sp")
        gridLayout.add_widget(mdCard)
        mdCard.add_widget(box1)
        box1.add_widget(deneme_card)
        deneme_card.add_widget(image)
        mdCard.add_widget(box2)
        box2.add_widget(box3)
        box3.add_widget(mdLabel1)
        box3.add_widget(mdLabel2)
        box3.add_widget(mdLabel3)
        box2.add_widget(box4)
        box4.add_widget(mdIconButton1)
        box4.add_widget(mdIconButton2)
    
    def download_mp3(self, id_index):
        url = self.url_list[id_index]
        yt = YouTube(url)
        yt.streams.get_by_itag(140).download("mp3","deneme.mp3")
        print("İndirildi")


    
    def download_mp4(self, id_index):
        url = self.url_list[id_index]
        yt = YouTube(url)
        yt.streams.get_by_itag(18).download("mp4","deneme.mp4")
        # yt.streams.get_highest_resolution().download("mp4","deneme.mp4")
        print("İndirildi")



        
    # def callback(self,instance):
    #     print('called from', instance.icon)

    def callback(self):
        print("geldi")


class Store(Screen):
    def __init__(self,**kwargs):
        super(Store,self).__init__(**kwargs)


    
    # def store_create_blog(self, title, image_name):
    #     print("ı write from store",title,image_name)
    #     print("I can't create in gridlayout with title and image_name from Download Class but I can write this info. ")
    #     a = self.ids.grd_storePage
    #     mdcard = MDCard(padding=10)
    #     image = Image(source=image_name)
    #     mdlabel = MDLabel(text=title)
    #     a.add_widget(mdcard)
    #     mdcard.add_widget(image)
    #     mdcard.add_widget(mdlabel)
        



class Favorite(Screen):
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
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        # self.theme_cls.primary_hue = "200"
        return ScreenManagement()
    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

login().run()