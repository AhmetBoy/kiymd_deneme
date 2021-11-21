from selenium import webdriver
from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
Window.size = (300,500)
a = Options()
a.headless = True

class Myt(BoxLayout):
    def __init__(self,**kwargs):
        super(Myt,self).__init__(**kwargs)
        
        self.browser = webdriver.Firefox(options=a)
        self.browser.get("https://www.ulasimpark.com.tr/kocaeli-kart")
        self.yaz()

    def yaz(self):
        f = open("kart_id.txt","r")
        self.ids.kentkart_id.text = f.read()
        f.close()

    def kaydet(self):
        kartNo = self.ids.kentkart_id.text
        f = open("kart_id.txt","w")
        f.write(kartNo)
        f.close()

    def kart_num(self):
        kartNo = self.ids.kentkart_id.text
        if len(kartNo) != 10:
            print("lütfen doğru girdiginizden emin olun.")
            self.ids.bakiye.text = "lütfen doğru girdiginizden emin olunuz."
            self.ids.dolumMiktari.text = ""
            self.ids.dolumTarihi.text = ""
            self.ids.kullanimTarihi.text = ""
        else:
            kartNo1 = kartNo[:5]
            kartNo2 = kartNo[5:]
            self.click(kartNo1,kartNo2)


    def click(self,kartNo1,kartNo2):
        kart_id1 = self.browser.find_element_by_xpath('//*[@id="kartNo1"]')
        kart_id2 = self.browser.find_element_by_xpath('//*[@id="kartNo2"]')
        btn_check = self.browser.find_element_by_xpath('//*[@id="btnSorgula"]')
        kart_id1.send_keys(kartNo1)
        kart_id2.send_keys(kartNo2)
        btn_check.click()
        time.sleep(1)
        money = self.browser.find_element_by_xpath('//*[@id="h3"]').text
        dolumMiktari = self.browser.find_element_by_xpath('//*[@id="dolumMiktari"]').text
        sonDolumTarihi = self.browser.find_element_by_xpath('//*[@id="sonDolumTarih"]').text
        sonKullanimTarihi = self.browser.find_element_by_xpath('//*[@id="sonKullanimTarih"]').text
        self.data(money,dolumMiktari,sonDolumTarihi,sonKullanimTarihi)



    def data(self,money,dolumMiktari,sonDolumTarihi,sonKullanimTarihi):  
        new_money =money[:-3]       
        self.ids.bakiye.text = "Kart Bakiyesi\n" + new_money + " ₺"
        # self.ids.bakiye.theme_text_color = "Primary"
        self.ids.dolumMiktari.text = "Son Dolum Miktarı\n" + dolumMiktari + " ₺"
        self.ids.dolumTarihi.text = "Son Dolum Tarihi\n" + sonDolumTarihi
        self.ids.kullanimTarihi.text = "Son Kullanım Tarihi\n" + sonKullanimTarihi
        self.browser.refresh()
        self.kaydet()



    def on_request_close(self, *args):
        self.browser.close()
        time.sleep(1)
        print("asdasd")
        return False

class deneme(MDApp):
    def build(self):
        Window.bind(on_request_close=Myt().on_request_close)
        return Myt()

deneme().run()