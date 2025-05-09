from urllib import response
from flask import request
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import os
import psutil as psu
import random
import time
import requests as req
import math
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import platform
import requests
from googlesearch import search
import speedtest 

#Metinden Sese Dönüştürme
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 7 == hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("have a nice day!")
    elif 0 == hour <=6:
        speak("Good Night!")
    else:
        speak("Good Evening!")

    speak("I  am  your voice  assistant, how  can I  help you?")
    
def timer():
    print("Kronometreyi enter tuşuna basarak başlatabilirsiniz/durdurabilirsiniz.")
    input()
    start_time = time.time()
    print("Kronometre başladı.Durdurmak için enter tuşuna basın.")
    input()
    end_time=time.time()
    elapsed_time=end_time-start_time
    print(f"Geçen süre {elapsed_time:2f} saniye")
    
def writing_heart():
    t=np.linspace(0,2*np.pi,1000)
    x=16 * np.sin(t)**3
    y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.figure(figsize=(6,6))
    plt.plot(x,y,color="red")
    plt.title("Heart")
    plt.axis("equal")
    plt.axis("off")
    plt.show()
    

def location():
    response = req.get('https://ipinfo.io/')
    data = response.json()
    city=data.get("city")
    region = data.get("region")
    country=data.get("country")
    print(f"Şehir: {city}, Bölge: {region}, Ülke: {country} ")
    
def kur():
    try:
        response=requests.get("https://api.exchangerate-api.com/v4/latest/TRY") #Api İle Güncel Kurların Verilerini Çek
        rates=response.json()['rates']
        return{
            "USD":round(1/rates["USD"],2),
            "EUR":round(1/rates["EUR"],2),
            
        }    
    except Exception as e:
        return 
    
def anaKur():
    rates=kur()
    if rates:
        print(f"1 USD={rates['USD']} TL")
        print(f"2 EUR={rates['EUR']} TL")
    else:
        print("Kur Bilgisi Alınamadı")
        
if __name__ == "__main" :
    anaKur()
    

    
def get_Location():
     response = req.get('https://ipinfo.io/')
     data = response.json()
     loc = data.get("loc")
     if loc:
         latitude,longitude=loc.split(",")
         map_url=f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
         print(f"Google Haritalar'da Aç :{map_url}")
         wb.open(map_url)
     else:
        print("Hata")

def shutdown():
    sistem = platform.system().lower()
    try:
        if sistem=="windows": #Eğer Sistem Windows İse
            os.system("shutdown /s /t 1")
        elif sistem == "Linux" or sistem=="Darwin": #Eğer Sistem Linux İse
            os.system("shutdown -h now")
        else:
            print("Desteklenmeyen işletim sistemi!")
    except Exception as e:
        print(f"Hata Oluştu:{e}")

def search_google():
    sorgu = speak("Ne Aramak İstersin:")

    try:
        print("\n Sonuçlar Getiriliyor...\n")

        for url in search(sorgu,num_results=5,lang="tr"):
            print(f"Bulunan Url:{url}")
            wb.get().open(url) #Aranan Şeyi Tarayıcıda Aç


    except Exception as e:
        print(f"Hata! {e}")
        
if __name__=="_main":
    search_google()
    
def scannow():
   try:
       process=subprocess.run(["sfc","/scannow"],check=True,text=True,shell=True)
       print("Tarama Tamamlandı.")
   except subprocess.CalledProcessError as e:
       print("Hata! {e}")
   except Exception as e:
       print("Hata {e}")
       
       


def speed_test():
    test=speedtest.SpeedTest()
    print("Sunucu Listesi Yükleniyor....")
    test.get_servers
    print("En Uygun Sunucu Aranıyor...")
    bestserver=test.get_best_server()
    print("Sunucu Bilgileri")
    print("Ülke: ", bestserver['country'])
    print("Şehir: ", bestserver['name'])
    print("Sağlayıcı: ", bestserver['sponsor'])
    print("Sunucu: ", bestserver['host'])
    print("-"*45)
    download=test.download()
    upload=test.upload()
    ping=test.results.ping
    print(f"\nDownload: {download / 1024 / 1024:.2f} Mbit/s")
    print(f"\nUpload: {upload / 1024 / 1024:.2f} Mbit/s")
    print(f"\nPing: {ping}")
    
if __name__ =="_main":
    speed_test()
    

def namaz_vakitleri():
    sehir = location()
    ulke="Turkey"
    api_url=f"http://api.aladhan.com/v1/timingsByCity?city={sehir}&country={ulke}&method=13"
    response=requests.get(api_url)
    data=response.json()
    tarih=data['data']['date']['gregorian']['date']
    vakitler=data['data']['timings']
    print(f"{sehir} için {tarih} tarihli namaz vakitleri:\n")
    for vakit,saat in vakitler.items():
        print(f"{vakit}:{saat}")  

def take_command(): #Komut Alma 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listen...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Algılanıyor...")
        query = recognizer.recognize_google(audio, language='tr-TR') #Komut Dilini Türkçe Olarak Ayarla
        print(f"Şunu dediniz: {query}\n")

    except Exception as e:
        print("Lütfen tekrar edin.") #Cümle Anlaşılmazsa
        speak("I Don't Understand")
        return "None"
        
    return query.lower()

if __name__ == "__main__":
    greet_user()
    
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Wikipedia\'da arama yapılıyor...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Wikipedia'ya göre")
            print(results)
            speak(results)
        
        elif 'web sitesini aç' in query:
            speak("Hangi web sitesini açmak istersiniz?")
            site_name = take_command()
            wb.open(f"http://{site_name}.com")
            speak(f"{site_name} açılıyor.")
        
        elif "dosyaları tara" in query:
            scannow()
            print("Taranıyor..")
            
            
        elif "konumumu bul" in query:
            speak("Searching for your location..")
            location()
            break
        
        elif "konumumu göster" in query:
            speak("Opening Maps...")
            get_Location()
            break
        
        elif "hava kaç derece" in query:
            wb.open("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Ankara")
            break
 
        elif "namaz vakitleri" in query:
            namaz_vakitleri()
            break
            
        elif "tarayıcıda arama yap" in query:
            speak("Aranacak Şeyi Söyleyin:")
            aranacak_sey=take_command()
            wb.open(f"https://{aranacak_sey}.com")
            break
        
        elif "kalp çiz" in query:
            speak("Writing Hearts..")
            print("Kalp Çiziliyor..")
            writing_heart()
            break
        
        elif "hız testi yap" in query:
            speed_test()
            break
        
        elif "google araması yap" in query:
            search_google()
            break
        
        elif "do a google search" in query:
            search_google()
            break
        
                       
        elif "virüs taraması yap" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure")
            os.startfile("mrt.exe")
            break
        
        elif "ağ bağlantılarını göster" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure")
            os.startfile("ncpa.cpl")
            break
        elif "kullanıcı hesaplarımı göster" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure")
            os.startfile("netplwiz.exe")
            break
        
        elif "denetim masasını aç" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure")
            os.startfile("control.exe")
            break

        elif "hesap makinesini aç" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure")
            print("Açılıyor..")
            os.startfile("calc.exe")
            break

        elif "not defterini aç" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure!")
            print("Açılıyor..")
            os.startfile("notepad.exe")
            break
        
        elif 'saat kaç' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Saat şu anda {strTime}")
        
        elif 'bugünün tarihi' in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            print(strDate)
            speak(f"Bugünün tarihi {strDate}")
        
        elif 'nasılsın' in query:
            speak("I'm fine.Thank You !")
            print("İyiyim ! Siz Nasılsınız ?")
        
        elif  "e-posta gönder" in query:
            print("Gmail Açılıyor...")
            wb.open("https://mail.google.com/mail/u/2/#inbox?compose=new")
            break
        

     
        elif "görüşürüz" or "görüşmek üzere" in query:
            speak("See You")
            break

        elif 'tarayıcıyı aç' in query:
            speak("Sure!")
            print("Açılıyor..")
            os.startfile("chrome.exe")
            break

        elif "görev yöneticisini aç" in query:
            speak("Sure!")
            print("Açılıyor..")
            os.startfile("taskmgr.exe")
            break
        
        #Her Kullanıcıda Çalışmaz
        elif "oyunu aç" in query:
            oyunun_yolu = "C:\\Users\\Necmettin\\Downloads\\yilanoyunproje.exe"
            subprocess.run([oyunun_yolu])

        elif "sistem bilgilerini göster" in query: #Sadece Windows İçin Çalışıyor
            speak("Sure!")
            print("Açılıyor..")
            os.startfile("msinfo32.exe")
            break

        elif "not al" in query:
            speak("Ne Yazmamı İstiyorsun?")
            note = take_command()
            file=open("notlar.txt","a")
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            file.write(f"{strTime}")
            file.write(":-")
            file.write(note+"\n")
            speak("Not aldım")
            break
        
        elif "{gelismisArama}" in query:
            gelismisArama=take_command()
            wb.open(gelismisArama)
            
        
        elif "seni hangi dil ile yazdılar" in query:
            speak("They wrote me in Python Programming language.")
            print("Beni Pyhton Programlama  Dili İle Yazdılar.")
            break

        elif "nerelisin" in query:
            speak("Ben bir sesli asistanım.Bu yüzden bir memleketim yok :)")
            print("Ben bir sesli asistanım.Bu yüzden bir memleketim yok :)")
            break

        elif "bugün hangi gün" or "bugün günlerden ne" in query:
            today = datetime.datetime.now().strftime("%A")
            print(today)
            speak(today)
            break

        elif "teşekkürler" in query:
            speak("You're welcome")
            break
        
        elif "kaç yaşındasın" in query:
            speak("Ben bir sesli asistanım.O yüzden bir yaşım olduğumu söylemem.Ancak 2024 yılında yapılmaya başlandım.")
            print("Ben bir sesli asistanım.O yüzden bir yaşım olduğumu söylemem.Ancak 2024 yılında yapılmaya başlandım.")

        elif "mesaj göndermek istiyorum" in query:
            speak("Sure!")
            print("Açılıyor..")
            wb.open("https://web.whatsapp.com")
            break
      
        elif "komut sayfasını aç" in query:
            speak("Sure!")
            print("Açılıyor..")
            os.startfile("cmd.exe")
            
        elif "dolar kaç lira" in query:
            anaKur()
            kur()
            break

        elif "rastgele bir sayı söyle" in query:
            rastgele = random.randint(0,100)
            print(rastgele)
            speak(rastgele)
            break
            
        
        elif "kronometre başlat" in query:
            speak("Sure!")
            timer()
            break
        
        elif "bilgisayarı kapat" in query:
            speak("Closing the Computer...")
            shutdown()
            break
        

        elif "bana bir hikaye anlat" in query:
            speak("Annesi küçük oğlunu bakkala yumurta almaya göndermiş. Bakkaldaki amcadan yumurta isteyince o da en küçük yumurtaları çocuğu vermiş. Çocuk yumurtalara şöyle bir bakmış ve: Bana Neden Hep Küçük Yumurtaları Veriyorsun ? Taşıması Kolay Olur Da Ondan Demiş bakkal. Oldukça zeki olan çocuk eksik para verip bakkaldan çıkmışBakkal arkasından bağırmış.Eksik Para verdin Çocuk Gülmüş ve Sayması kolay olur da ondan  ")
            break
        
        elif "matematik işlemi yap" in query:
            speak("Sure, which operation would you like to perform?")
            print("İşlem Seçin : (1:Topla 2:Çıkar 3:Böl 4:Çarp 5:Üs Alma 6:Kare Al)")
            islemSec=int(input(":"))
            
            if islemSec==1:
                a=int(input("Birinci Sayı:"))
                b=int(input("İkinci Sayı:"))
                sonuc = a+b
                print(sonuc)
                speak(sonuc)
                break
            
            elif islemSec==2:
                a=int(input("Birinci Sayı:"))
                b=int(input("İkinci Sayı:"))
                sonuc = a-b
                print(sonuc)
                speak(sonuc)
                break
            
            elif islemSec==3:
            
                a=int(input("Birinci Sayı:"))
                b=int(input("İkinci Sayı:"))
                sonuc = a/b
                print(sonuc)
                speak(sonuc)
                break
               
            elif islemSec==4:
                a=int(input("Birinci Sayı:"))
                b=int(input("İkinci Sayı:"))
                sonuc = a*b
                print(sonuc)
                speak(sonuc)
                break    
            
            elif islemSec==5:
                a=int(input("Taban:"))
                b=int(input("Üs:")) 
                sonuc = math.pow(a,b)
                yuvarlamak = math.floor(sonuc)
                print(yuvarlamak)
                speak(yuvarlamak)
                break
            
            elif islemSec==6:
                a=int(input("Sayıyı Girin:"))
                sonuc = math.sqrt(a)
                print(sonuc)
                speak(sonuc)
                break
       
            
            
          
     
        
        
        
  

   

      



        
    
      


  
                

            
 