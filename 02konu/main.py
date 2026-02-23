""" 
Gömülü Fonksiyonlar / En Çok Kullanılan Gömülü Fonksiyonlar / Fonksiyon ve Metotların Farkı

Gömülü Fonksiyonlar: Python’da hazır gelen, bizim ayrıca tanımlamamıza gerek olmayan fonksiyonlardır.
                     Python kurulunca otomatik gelirler. Ekstra import yapmamız gerekmez.


En Çok Kullanılan Gömülü Fonksiyonlar
1- print()  -> Ekrana çıktı verir
2- type()   -> Datanın veri türünü gösterir.
3- isinstance(parametre, data türü) -> Veri tipi kontrolü yapar. true / false sonucu döner.
4- len()    -> Datanın uzunluğunu verir.
5- int(), float(), str()    -> Datanın tip dönüşümünü sağlar.
6- input()  -> Kullanıcıdan veri alır. Not: Alınan bilgi her zaman string data type'ındadır.
7- max() / min()    -> En büyük ve en küçük değeri verir.
8- sum()    -> Toplama yapar.
9- abs()    -> Mutlak değer alır.
10- round()  -> Yuvarlama yapar.
11- range() -> Döngülerde çok kullanılır. aralık belirlemek için kullanılır.
12- sorted() -> Sıralama yapar.

Fonksiyon ve Metotların Farkı
Fonksiyonlar bağımsızdır, metotlar bir nesneye bağldır.
örn: len() bir fonksiyon olup nesne.upper() metotdur.

"""

isim = 'Hayko Cepkin'
print(isim)
print('İsim değişkeninin data türü: ', type(isim))
print('İsim değişkeninin uzunluğu: ', len(isim))

sayi = '50'
print(type(int(sayi)))
print(type(float(sayi)))

print('Integer mi? ',isinstance(5,int))

dogumYili= input('Doğum Yılınızı Girin: ')
## print('Yaşınız: ', 2026 - dogumYili)     ##Input'tan alınan veri satı dahi olsa string çalışacağı için hata verir.
print('Yaşınız: ', 2026 - int(dogumYili))

print(max(10,50,45))    ##Ekrana 50 yazar
print(min(10,50,45))    ##Ekrana 10 yazar


topla = sum([10,50,45])     ##Toplama işleminin olması için datanın liste, tuple, range, set data türünde birden fazla veri içeriyor olması gerekiyor.
print(topla)

mutlak = abs(-5)
print(mutlak)       ## Ekrana 5 yazar

ondalikli = 42.5785
print(round(ondalikli))     # Ekrana 43 yazar
print(round(ondalikli,2))   # Ekrana 42.58 yazar

aralik = range(5)
print(aralik)
print(sum(aralik)) #0'dan başlar 5'i dahil etmenden sayıları toplar. 0+1+2+3+4 = 10

for i in range(3):
    print('Mahmut Tuncer') #Ekrana 3 defa Mahmut Tuncer yazar

karmanCorman = [1,2,8,96,46,186,11]
print(sorted(karmanCorman))