""" 
Sözlükler (Dict)

- Sözlükler anahtar-değer (key-value) mantığıyla çalışan veri tipidir.
- {} süslü parantezler içinde oluşturulurlar.
- Bir değere ulaşmak için dictAdi['keyAdi'] şeklinde kullanılmalı.

Liste → index ile erişilir
Sözlük → anahtar (key) ile erişilir

kisi = {
    "isim": "Hayko",
    "yas": 47,
    "meslek": "Sanatçı"
}

"isim"  -> Key
"Hayko" -> Value

*** Dict içine yeni Eleman Ekleme ve Güncelleme ***
kisi['soyisim'] = 'Cepkin'  -> Yeni key ve value ekler
kisi['yas'] = 50            -> yas key'ine ait veriyi günceller


*** Dict içinde Eleman Silme ***
del dictAdi["keyAdi"] veya dictAdi.pop('keyAdi')


*** Dict Metotları ***
- keys()    -> Tüm key'leri verir.
- values()  -> Tüm value'ları verir.
- items()   -> Aynı anda hem key hem de value'ları verir. for döngüsünde çok kullanılır.
- update()  -> Sözlüğü toplu günceller.
- pop('keyAdi')     -> ilgili key'i ve value'sunu siler
- popitem() -> Son elemanı siler.
- copy()    -> Dict'i kopyalar
- clear()   -> Tüm sözlüğü boşlatır.
- setdefault('olmayan key','Gelecek olan Değer') -> Eğer ilgili key yoksa oluşturup varsayıaln bir değer ataması yapar

"""

kisi = {
    "isim": "Hayko",
    "yas": 47,
    "meslek": "Sanatçı"
}

print(kisi["isim"])                         ## Ekrana 'Hayko' Yazar.
## print(kisi["soyisim"])                   ## Hata Verir. Bu noktada .get(() metodu kullanımı iyi olacaktır.
print(kisi.get('soyisim','Bulunamadı'))     ## Ekrana 'Bulunamadı' yazar.

kisi['soyad'] = 'Cepkin'        
print(kisi)                     # Ekrana {'isim': 'Hayko', 'yas': 47, 'meslek': 'Sanatçı', 'soyad': 'Cepkin'} döner

kisi["yas"] = 50                
print(kisi)                     # Ekrana {'isim': 'Hayko', 'yas': 50, 'meslek': 'Sanatçı', 'soyad': 'Cepkin'} döner


del kisi["meslek"]
print(kisi)                     # Ekrana {'isim': 'Hayko', 'yas': 50, 'soyad': 'Cepkin'} yazar
kisi.pop('yas')
print(kisi)                     # Ekrana {'isim': 'Hayko', 'soyad': 'Cepkin'} yazar

print(kisi.items())             # dict_items([('isim', 'Hayko'), ('soyad', 'Cepkin')])

for key,value in kisi.items():
    print(key,value)


kisi.update({"isim":'Mahmut', "soyad":"Tuncer"})
print(kisi)


kisi["meslek"] = 'Sanatçı'
kisi['dogum'] = 1970
print(kisi)         #Ekrana {'isim': 'Mahmut', 'soyad': 'Tuncer', 'meslek': 'Sanatçı', 'dogum': 1970} yazar

kisi.popitem()      
print(kisi)         #Ekrana {'isim': 'Mahmut', 'soyad': 'Tuncer', 'meslek': 'Sanatçı'} yazar

yeniKisi = kisi.copy()
print(yeniKisi["isim"])     #Ekrana 'Mahmut' yazar
print(yeniKisi)     #Ekrana {'isim': 'Mahmut', 'soyad': 'Tuncer', 'meslek': 'Sanatçı'} yazar.

kisi.clear()        #Tüm datayı temizler
print(kisi)         #Ekrana {} yazar


""" Dict datasının For Döngüsü Kullanımı """
for anahtar in yeniKisi.keys():         #for anahtar in yeniKisi: ile alternatif kullanılabilir.
    print(anahtar)                      #Ekrana key isimlerini tek tek yazar

for degerler in yeniKisi.values():
    print(degerler)                     #Ekrana value'ları tek tek yazar


""" İç İçe Dict Kullanımı (Nested Dict) """

kullanici = {
    'user1': {"user":'hayko',"pass":123,"isim":'Hayko','soyisim':'Cepkin'},
    'user2': {"user":'mamo',"pass":456,"isim":'Mahmut','soyisim':'Tuncer'}
}

for key,value in kullanici["user1"].items():
    print(f'{key}: {value}')

for anahtar,deger in kullanici.items():
    print(f'{anahtar}: {deger}')


kadi = input('Kullanıcı Adınızı Girin')

for antr,dgr in kullanici[kadi].items():
    print(f'{antr}: {dgr}')


##### Örnek #####
"""
1- Fiyatı 900 yap
2- Yeni key ekle: "kategori": "Supplement"
3- Stok değerini ekrana yazdır
4- Tüm key-value çiftlerini for döngüsüyle yazdır
"""

urun = {
    "ad": "Protein Tozu",
    "fiyat": 850,
    "stok": 20
}

urun["fiyat"] = 1000
urun['kategori'] = "Supplement"
print(urun["stok"])
for key,value in urun.items():
    print(f'{key.capitalize()}: {value}')