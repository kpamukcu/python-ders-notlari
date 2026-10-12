""" 
NumPy Nedir?
NumPy, Python'da sayısal verileri depolamak, hesaplamak, dönüştürmek ve analiz etmek için kullanılan bir kütüphanedir. NumPy = Numerical Python
Özellikle çok büyük liste datalar için kullanımı tercih edilir.

Örneğin bir işletmenin 100.000 reklam kampanyası kaydı, bir koşucunun binlerce nabız ölçümü veya bir e-ticaret sitesinin günlük satış verileri olduğunu düşün.

Bu veriler üzerinde şu işlemleri yapılabilir:
Ortalama, toplam, minimum ve maksimum hesaplamak.
Birden fazla değere aynı matematiksel işlemi uygulamak.
Belirli koşulları sağlayan verileri filtrelemek.
Verileri satır ve sütunlardan oluşan yapılar hâlinde düzenlemek.
İstatistiksel hesaplamalar yapmak.
Makine öğrenmesi ve bilimsel hesaplamalar için verileri hazırlamak.

Dijital pazarlama ve reklam analizi

Google Ads veya Meta Ads raporlarından elde ettiğin tıklama, gösterim, maliyet ve dönüşüm verilerini analiz edebilirsin.

Örneğin:

Kampanyaların ortalama tıklama maliyetini hesaplamak.
Maliyetleri belirli bir katsayıyla güncellemek.
Belirli bir maliyetin üzerindeki kampanyaları filtrelemek.
Günlük performans değişimlerini hesaplamak.

- Sayısal işlemleri dizinin tüm elemanlarına doğrudan uygulayabiliriz.


Bazı metot ve fonksiyonlar:
- np.array(...)         -> Python listesini Numpy dizisine dönüştürür.
- degiskenAdi.ndim      -> Dizinin kaç boyutlu olduğunu gösterir.
- degiskenAdi.shape     -> Dizinin boyut yapısını gösterir.
"""

import numpy as np

## Örnek1 -> Liste datanın içindeki her parametreyi 2 ile çarpmak
#Standart Python Yapısı
paces = [300,315,290]
paces = paces *2
print(paces)        ## [300, 315, 290, 300, 315, 290] çıktısını verir. 

paces = np.array([300,315,290])
paces = paces *2
print(paces)        ## [600 630 580] çıktısını verir.
print(type(paces))  ## <class 'numpy.ndarray'> çıktısını verir.
print(paces.ndim)   ## 1 çıktısını verir.
print(paces.shape)  ## (3,) çıktısını verir. 3 elemenlı tek boyutlu dizi anlamına gelir.

## Örnek 2 - Mini Soru
# durations adında, [52, 49, 55, 47, 51] değerlerini içeren bir NumPy dizisi oluştur.
# Diziyi ekrana yazdır.
# Veri yapısının türünü ekrana yazdır.
# Dizinin boyut sayısını ekrana yazdır.
# Dizinin şeklini ekrana yazdır.
# Son olarak dizideki her değeri ikiyle çarp ve sonucu ekrana yazdır.

durations = np.array([52,49,55,47,51])
print(durations)
print(type(durations))
print(durations.ndim)
print(durations.shape)
durations = durations * 2
print(durations)


""" 
Vektörel İşlemler?
Vektörel işlemler, bir dizideki çok sayıda elemana işlemi tek tek döngüyle uygulamak yerine, işlemi doğrudan dizi üzerinde gerçekleştirmemizi sağlar. Buradaki kritik nokta şu: Bir satır kodla birden fazla veri üzerinde aynı işlemi yapabiliriz.

Örneğin: 
paces = np.array([300,315,290])
paces = paces *2                ## Bütün elemanları standart Python döngüsüne almadan 2 ile çarpar.

Matematiksel işlemler vektörel işlem olduğu gibi karşılaştırma işlemleri de dizi üzerinde uygulanabilir.
"""

paces = np.array([300,315,290,305,310])
paces = paces < 305
print(paces)        ##[True False  True False False] çıktısını verir.

# Örnek 3 - Mini Soru
durations = np.array([52,49,55,47,51])

# Her süreye 3 ekle
# Her süreyi 2 ile çarp
# Her süreden 5 çıkar
# Hangi sürelerin 50'den küçük olduğunu bul.

print(durations + 3)
print(durations * 2)
print(durations - 5)
print(durations < 50)


## Vektörlerde parametrelere indisNo'lar ile ulaşılabilir. İndisNo'lar 0'dan başlar.
paces = np.array([300,315,290,305,310])
print(paces[2])     #Ekrana 290 yazar.

## Vektörlerde dilimleme (Slicing)
## dizi[başlangıçİndisNo : bitişİndisNo]    -> başlangıç değeri dahil olup bitiş değeri dahil değildir.
print(paces[1:4])   ## [315,290,305]
print(paces[:3])    ## indis 0'dan şalar idnis 2'de biter [300,315,290]
print(paces[2:])    ## indis 2'den başlar sonuna kadar yakalar. [290,305,310]
print(paces[:])     ## Tümünü getirir
print(paces[::2])   ## indisin 2 adım büyüklüğünü belirtir. Yani bir elemanı alıp bir eleman atlayarak ilerler

paces[1] = 320      ## indis 1'in değeri 320 olarak değişti
print(paces)        ## [300,320,290,305,310]

paces[1:3] = [325,295]  ## indis 1 ve 2'nin değerlerini 325 ve 295 olarak değiştirdi.
print(paces)        ## [300,325,295,305,310]

## Vektörelerin Temel Metotları ve Özellikleri
paces = np.array([300,315,290,305,310])

print(paces.min())          ## NumPy dizi datası içindeki en küçük değeri verir
print(paces.max())          ## NumPy dizi datası içindeki en büyük değeri verir
print(paces.mean())         ## NumPy dizi datası içindeki bütün değerlerin ortalamasını verir.
print(paces.sum())          ## NumPy dizi datası içindeki bütün değerlerin toplamını verir
print(np.sort(paces))       ## NumPy dizi datası içindeki değerleri küçükten büyüğe doğru sıralayarak yeni dizi data döndürür.


## Örnek 4 - Mini Soru
paces = np.array([300,315,290,305,310])

## İlk elemanı yazdır.
## Son elemanı yazdır.
## İkinci, Üçüncü ve dördüncü elamanları seç
## Her iki elemandan birini seçerek yeni ir çıktı oluştur.
## Dizinin en küçük ve en büyük değerlerini yazdır.
## Dizinin ortalamasını hesapla
paces = np.array([300,315,290,305,310])
print(paces[0])
print(paces[-1])
print(paces[2:5])
print(paces[::2])
print(paces.min())
print(paces.max())
print(paces.mean())