import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum="Açık"
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):            
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon Kapanıyor...")
            self.tv_durum="Kapalı"
    def ses_ayarları(self):

        while True:
            cevap = input("Sesi azalt :'<'\nSesi arttır : '>'\nÇıkıs : çıkıs")
            if (cevap == '<'):
                if (self.tv_ses != 0):
                    
                    self.tv_ses-=1,
                    print("Ses : ",self.tv_ses)
            elif (cevap == '>'):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses : ",self.tv_ses )        
            else:
                print("Ses güncellendi...",self.tv_ses)
                break
    def kanal_ekle(self,yeni_kanal):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(yeni_kanal)

        print("Kanal eklendi.")
    def rastgele_kanal(self,):
        rastegele =random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastegele]

        print("Şuanki Kanal : ",self.kanal) 
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durum : {}\nTV Ses : {}\nKanal Listesi : {}\nKanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda ()



print("""

       Televizyon Uygulaması
   1.TV Aç

   2.Tv Kapat         

   3.Ses Ayarları

   4.Kanal Ekle

   5.Kanal Sayısını Öğrenme

   6.Rastgele Kanala Geçme

   7.Televizyon Bilgileri

   Çıkmak için 'q' basınız. 

       """)


while True:
    işlem = input ("İşlem Seçiniz:")
    if (işlem == 'q'):
        print("Program Sonlandırılıyor...")
        time.sleep(2)
        print("Program Sonlandırıldı.")
        break
    elif(işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimieri = input("Kanal isimlerini ',' ayırarak girin.")

        kanal_listesi = kanal_isimieri.split(",")  
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem")























            




















