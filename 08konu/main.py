""" 
Modüller -> İçinde fonksiyonların olduğu tek bir .py dosyasıdır.
import edilerek içindeki fonkyironlar kullanılabilir.

Kütüphane -> Birden fazla modülün bir araya gelmesi ile oluşur.
Framework -> Framework daha büyük bir yapıdır. Sana bir sistem sunar ve sen onun kurallarına göre kod yazarsın.
            Kütüphanede sen çağırırsın, framework seni çağırır.

            Örneğin:
            Web framework: Django
            API framework: Flask

            Framework’te yapı hazırdır: klasör yapısı, ayarlar, routing sistemi, veri tabanı bağlantısı

            Sen sadece kurallara uygun kod yazarsın.

"""
#Custom Modül Kullanımı
import matematik                #matematik dosyası main.py dosyasına yüklendi. 
matematik.topla(5,3)

## ---------------------------------------- ##
#### HAZIR KÜTÜPHANELER (RANDOM & DATETIME) ####
#### RANDOM KÜTÜPHANESİ ####

import random                   #Ön tanımlı random modülü main.py dosyasına yüklendi.

#randint()  Rastgele sayı üretir. iki parametre alır.
print(random.randint(1,10))   

#random()   Rastgele 0 ile 1 arasında ondalıklı sayı üretir. Parametre almaz.
print(random.random())          

#choise() -> liste data içinde rastgele değer seçer.
kura = ['Hayko','Mahmut','Ajdar']
print(random.choice(kura))      

#shuffle() -> Liste içindeki değerleri karıştırır.

userID = ['453','454,','455','456','457']
random.shuffle(userID)          
print(userID)

""" 

Random Kütüphanesi Gerçek hayat Örnekleri

| Fonksiyon                   | Açıklama                                                    | Gerçek Hayatta Kullanım Örneği                                                    | Örnek Kod                                               |
| --------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `random.randint(a, b)`      | a ile b arası **tam sayı** üretir                           | Zar atma, rastgele yaş veya puan seçme                                            | `zar = random.randint(1,6)`                             |
| `random.random()`           | 0 ile 1 arasında **ondalıklı sayı** üretir                  | Olasılık simülasyonu, şans hesaplama                                              | `s = random.random()`                                   |
| `random.choice(list)`       | Listeden **tek rastgele eleman** seçer                      | Rastgele soru seçme, çekiliş, rastgele isim                                       | `secim = random.choice(["Ali","Ayşe","Mehmet"])`        |
| `random.choices(list, k=n)` | Listeden **n adet rastgele eleman (tekrar olabilir)** seçer | Şifre oluşturma, rastgele menü seçme                                              | `sifre_karakterleri = random.choices(karakterler, k=8)` |
| `random.sample(list, k)`    | Listeden **n adet benzersiz eleman** seçer                  | Çekilişte birden fazla kazanan seçme, turnuva eşleşmesi                           | `kazananlar = random.sample(katilimcilar, 2)`           |
| `random.shuffle(list)`      | Listeyi **yerinde karıştırır**                              | Kart destesini karıştırma, playlist karıştırma, öğrencileri rastgele sıraya dizme | `random.shuffle(ogrenciler)`                            |
| `random.uniform(a, b)`      | a ile b arasında **ondalıklı sayı** üretir                  | Rastgele sıcaklık, rastgele fiyat belirleme                                       | `sicaklik = random.uniform(20.0, 30.0)`                 |
| `random.seed(n)`            | Rastgeleliği kontrol etmek için **başlangıç değeri** verir  | Testlerde aynı rastgele sonuçları tekrar üretmek                                  | `random.seed(42)`                                       |

"""


## ---------------------------------------- ##
## DATETIME KÜTÜPHANESİ ##
## Tarih ve saat işlemleri için kullanılır.
## Belirli bir tarih oluşturmak için datetime() fonksiyonu parametre alabilir. Ör: datetime(Yıl, Ay, Gün)

#import datetime                 # ön tanımlı datetime kütüphanesi import edildi
from datetime import datetime    # Ön tanımlı datetime kütüphanesinden datetime modülü import edildi.

simdi = datetime.now()  ## Şuanın tarih ve saat bilgisini yakalar.
print(simdi)

print(simdi.date())                 ## Şuanın sadece tarih bilgisini verir.
print(simdi.strftime("%d-%m-%Y"))   ## Tarih ve saat bilgisini istediğimiz formatta vermeyi sağlar.

""" 
| Kod | Anlamı |
| --- | ------ |
| %d  | Gün    |
| %m  | Ay     |
| %Y  | Yıl    |
| %H  | Saat   |
| %M  | Dakika |
"""

print(simdi.time())     ## Şuanın sadece saat bilgisini verir.

dogumGunu = datetime(1982,1,6)
print(dogumGunu)

t1 = datetime(1982,3,6)
t2 = datetime.now()

print(t2-t1)    #iki tarih arasındaki gün sayısını verir.



""" 
Örnek:
1 ile 100 arasında rastgele sayı üret.
Kullanıcı tahmin etsin.
Doğruysa “Kazandın” yazsın.
Yanlışsa tarih + saat ile birlikte “Yanlış tahmin” yazsın.
"""

sayi = random.randint(1,100)

while True:
    tahmin = int(input('1 ile 100 arasında bir sayı tahmin edin: '))
    if sayi == tahmin:
        print(f'{simdi.strftime("%d - %m - %Y / %H:%M")} - Doğru Tahmin')
        break
    else:
        print(f'{simdi.strftime("%d - %m - %Y / %H:%M")} - Yanlış Tahmin')
        devam = input('Tekrar Denemek İster misin? E / H: ').lower()
        if devam == 'h':
            print('Game Over')
            break
