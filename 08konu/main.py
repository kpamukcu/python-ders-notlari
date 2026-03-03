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

#Hazır Modül Kullanımı
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

