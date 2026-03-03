""" 
For Döngüsü (Loops)

Tekrarlanacak işlemler için kullanılır. Liste, Tuple, Sözlük, String vb dataların elemanları üzerinde tek tek işlem yapabilmeyi sağlar.

Genel Syntax
for degisken in data:
    Çalışacak kod Burada yazılır..

"""

## Liste data için for döngüsü
sayilar = [10,20,30,40,50]

for sayi in sayilar:
    print(sayi)    ## Ekrana sırasıya 10,20,30,40,50 yazar.

uyeler = ['Hayko Cepkin','Mahmut Tuncer', 'Bülent Ersoy', 'Yıldız Tilbe', 'Ajdar', 'Aleyna Tilki']

for uye in uyeler:
    print(uye)

## String Data için For Döngüsü
isim = 'Hayko Cepkin'
for harf in isim:
    print(harf)

##range() ile for döngüsü
for i in range(5):
    print(i)        #Ekrana 0 1 2 3 4 yazar. 5 dahil edilmez. 

for i in range(2,6):    #Birinci parametre başlangıç değeri olup ikinci parametre bitiş değerini belirler ancak bitiş değeri dahil değildir.
    print(i)        #Ekrana 2 3 4 5 yazar. 

for i in range(20,30,3):    #üçüncü parametre kaç kaç ilerleyeceğini belirler.
    print(i)                #Ekrana 20, 23, 26, 29 yazar.

""" 
Not:
✔ Belirli sayıda tekrar yapmak
✔ Sayısal aralık üretmek
✔ Index üzerinden işlem yapmak
✔ Sayaç mantığı kurmak
✔ Geri sayım yapmak
✔ Algoritma kurmak

"""

## indisli(indexli) dolaşmak - enumerate()
meyveler = ['Muz','Karpuz','Kivi']

for indis, meyve in enumerate(meyveler):
    print(indis,meyve)                      #Ekrana 0 Muz, 1 Karpuz, 2 Kivi yazar
    #print(f'{indis+1}- {meyve}')           #Ekrana 1- Muz, 2-Karpuz, 3-Kivi yazar

##Sözlük(Dict) Data için For Döngüsü
urun = {
    "ürün": "Robot Süpürge",
    "fiyat": 900,
    "stok": 25
}

for a,b in urun.items():
    print(f'{a.capitalize()}: {b}')         #Ekrana Ürün: Robot Süpürge, Fiyat: 900, Stok: 25 yazar.


""" 
Örnekler
1- 1’den 20’ye kadar çift sayıları yazdır
2- Bir listenin içindeki sayıların toplamını for ile hesapla
"""

#Örnek 1
for i in range(2,22,2):
    print(i)

#Örnek 2
sayilar = [10,20,30,40,50]
toplam = 0

for sayi in sayilar:
    toplam += sayi

print(toplam)
