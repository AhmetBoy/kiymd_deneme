from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.progressbar import ProgressBar
from kivymd.uix.imagelist import SmartTile
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.chip import MDChip
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.button import MDIconButton, MDFillRoundFlatIconButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
import urllib.request
import urllib.request, re, os, time
import threading
from kivymd.utils.fitimage import FitImage
from pytube import YouTube
from kivy.utils import platform
from kivy.clock import Clock
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

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
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        self.file_manager.preview = True
        

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        print(path)
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def make_therad(self):
        threading.Thread(target = self.make_search_id).start()  ####### FİRST THREAD FOR SEARCH İN YOUTUBE.
        

    def make_search_id(self, *args):
        searched_word = self.ids.search_word.text
        searched_word2 = searched_word.split(" ")
        searched_word3 = "+".join(searched_word2)
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searched_word3)
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
            lenght = yt.length
            thumbnail_url = "https://img.youtube.com/vi/"+str(i)+"/maxresdefault.jpg"

            # try:
            #     thumbnail_url = "https://img.youtube.com/vi/"+str(i)+"/maxresdefault.jpg"
            #     print(thumbnail_url)
            #     urllib.request.urlretrieve(thumbnail_url , image_name)
            # except:
            #     urllib.request.urlretrieve(yt.thumbnail_url , image_name)
            image_name_list.append(image_name)
            self.creat_blog(title, author, date, thumbnail_url, lenght, id_index)
            id_index += 1
            if id_index == 3:
                time.sleep(0.2) #gecikme olması laızm yoksa sondaki png yi silemiyor dosya hala kullanılıyor hatası veriyor.
                # self.delete_image(image_name_list)
                break
    
    # def delete_image(self, image_name_list):
    #     print("deletegeldi")
    #     for i in (image_name_list):
    #         try:os.remove(str(i))
    #         except:pass

    def creat_blog(self, title, author, date, thumbnail_url, lenght, id_index):
        gridLayout = self.ids.grd_downloadPage
        mdCard = MDCard(spacing=10, padding=[10,10], radius=[10], elevation=15)
        box1 = BoxLayout(size_hint_x=.4)
        deneme_card = MDCard(radius=[10],padding=5)
        image = SmartTile(source=str(thumbnail_url),box_color=(0,0,0,0),on_press=lambda x:self.open_youtube(id_index))
        mdLenght = MDLabel(text=str(str(round(lenght/60))+":0"+str(lenght//60)),size_hint=(None,None),size=(70,20),pos_hint={"center_x":.86,"center_y":.1},theme_text_color="Custom",halign="center",text_color=( 1, 1, 1, 1))
        self.box2 = BoxLayout(orientation="vertical", size_hint_x=.6)
        box3 = BoxLayout(orientation="vertical", pos_hint={"center_x":.5, "center_y":.9}, size_hint_y=.99)
        mdLabel1 = MDLabel(text=str(title),font_style="Body2",theme_text_color="Primary",bold=True)
        mdLabel2 = MDLabel(text=str(author),font_style="Caption",theme_text_color="Primary")
        # mdLabel3 = MDLabel(text=(str(date)+" "+str(lenght)),font_style="Body2",theme_text_color="Primary")
        # bar = ProgressBar(value=0)
        self.box4 = BoxLayout(spacing=4)
        mdIconButton1 = MDFillRoundFlatIconButton(on_press=lambda x:self.download_mp3_method(id_index), text="MP3", icon="youtube",user_font_size="48sp")
        mdIconButton2 = MDFillRoundFlatIconButton(on_press=lambda x:self.download_mp4_method(id_index), text="MP4", icon="youtube",user_font_size="48sp")
        gridLayout.add_widget(mdCard)
        mdCard.add_widget(box1)
        box1.add_widget(deneme_card)
        deneme_card.add_widget(image)
        image.add_widget(mdLenght)
        mdCard.add_widget(self.box2)
        self.box2.add_widget(box3)
        box3.add_widget(mdLabel1)
        box3.add_widget(mdLabel2)
        # box3.add_widget(mdLabel3)
        # self.box2.add_widget(bar)
        self.box2.add_widget(self.box4)
        self.box4.add_widget(mdIconButton1)
        self.box4.add_widget(mdIconButton2)
        self.ids.spinner.active = False

    def open_youtube(self,index):
        import pywhatkit
        pywhatkit.playonyt(str(self.url_list[index]))

    def download_mp3_method(self,i):
        threading.Thread(target = self.download_mp3,args=[i]).start()  ####### SECOND THREAD FOR DOWNLOAD MP3


    def download_mp4_method(self,i):
        threading.Thread(target = self.download_mp4,args=[i]).start()  ####### THİRD  THREAD FOR DOWNLOAD MP3

    
    def download_mp3(self,id_index, *args):
        try:
            print("suan geldi")
            self.ids.download_spinner.active = True
            url = self.url_list[id_index]
            yt = YouTube(url)
            yt.streams.get_by_itag(140).download("deneme.mp3")
            print("İndirildi")
            self.ids.download_spinner.active = False
            self.show_dialog("MP3")
        except:
            self.show_dialog("MP3 İndirme Yeri Hatası")
            self.ids.download_spinner.active = False



    def download_mp4(self,id_index, *args):
        # try:
        self.ids.download_spinner.active = True
        url = self.url_list[id_index]
        yt = YouTube(url)
        yt.streams.get_by_itag(18).download("deneme.mp4")
        print("İndirildi")
        self.ids.download_spinner.active = False
        self.show_dialog("MP4")
        # except:
        #     self.ids.download_spinner.active = False
        #     self.show_dialog("MP4 İndirme Yeri Hatası")


    def show_dialog(self,kind):
        self.dialog = MDDialog(title="Download Manager",text=(f"[color=#00FF00]{str(kind)} Downloaded.[/color]")).open()



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