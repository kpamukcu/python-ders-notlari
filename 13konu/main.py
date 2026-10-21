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
print(paces[0])
print(paces[-1])
print(paces[2:5])
print(paces[::2])
print(paces.min())
print(paces.max())
print(paces.mean())

print(np.size(paces))       # Parametre sayısını verir.

""" 
NumPy Matrisleri
Verileri satır ve sütunlar hâlinde düzenlemeyi ve analiz etmek. Matris, satır ve sütunlardan oluşan iki boyutlu sayısal bir yapıdır. NumPy'de bunu np.array() kullanarak oluşturabiliriz.

Bir matrisin yapısını anlamak için .ndim, .shape, .size özelliklerini kullanmalıyız.

"""

data = np.array([
    [300,315],
    [290,305]
])

print(data)

""" 
Çıktısı:
[[300 315]
 [290 305]]

Açıklama:
2x2(2 Satır x 2 Sütun) NumPy Matrisi
300 -> Satır 0 - Sütun 0
315 -> Satır 0 - Sütun 1
290 -> Satır 1 - Sütun 0
305 -> Satır 1 - Sütun 1
"""

print(data.ndim)    ## ndim     -> Boyut sayısnı verir.
print(data.shape)   ## shape    -> Satır ve Sütun sayısını verir.
print(data.size)    ## size     -> Toplam eleman sayısını verir.

## Örnek - Reklam Kampanyası
## Veri yapımız şöyle:
## Kampanya	    1. gün	2. gün
## Kampanya A	120	    150
## Kampanya B	80	    95
## Kampanya C	200	    180
## Burada her satır bir kampanyayı, her sütun ise bir günü temsil ediyor.
## Bu düzen, verileri karşılaştırmayı ve analiz etmeyi kolaylaştırır. İlerleyen derslerde bu matrisin toplamını, ortalamasını, belirli satırlarını ve koşulu sağlayan değerlerini hesaplayacağız.

clicks = np.array([
    [120,150],
    [80,95],
    [200,150]
])

print(clicks)
print(clicks.shape)

""" 
Matrislerde indeksleme
tek boyutlu dizilerde paces[0] ile bir elemana erişebiliyoruz ancak iki boyutlu dizilerde hem satır hem sütun belirtmeliyiz.
Ör: diziAdi[satirNo,sütunNo]
"""

print(clicks[0,0])  ## 120
print(clicks[0,1])  ## 150
print(clicks[1,0])  ## 80
print(clicks[2,1])  ## 150

print(clicks[0, :]) ## Bir satırın tamamını seçer [120,150]. ilk satırın tüm sütunlarını getirir.
print(clicks[:,0])  ## Bir sütunun tamamını seçer [120,80,200]. Tüm Satıların ilk sütunu getirir.

print(clicks[0:2, :])   ## İlk iki satırın tüm sütunlarını getirir.

""" 
Matrislerde Eleman Değiştirme
Bir elemanı değiştirmek için satır ve sütun indekslerini kullanırız.
"""

clicks[0,1] = 160   ## İlk satırın ikinci elemanı 150 yerine 160 oldu.
print(clicks)


## Örnek - Mini Uygulama

# 1. Matrisin boyut sayısını yazdır.    `ndim` kullan.
# 2. Matrisin şeklini yazdır.   `shape` kullan.
# 3. Toplam eleman sayısını yazdır. `size` kullan.
# 4. İlk haftanın tüm antrenmanlarını yazdır. İlk satırı seç.
# 5. İkinci haftanın üçüncü antrenmanını yazdır. İndekslerin sıfırdan başladığını unutma.
# 6. Bütün haftaların ilk antrenmanlarını yazdır. Sütun seçmek için `:` kullan.
# 7. Üçüncü haftanın ikinci antrenmanını 7 yerine 8 yap. İlgili elemanı değiştir ve matrisi tekrar yazdır.

weekly_km = np.array([
    [5,8,10],
    [6,9,12],
    [4,7,11]
])



print(weekly_km.ndim)   ## Boyut Sayısı     /   2 Boyut
print(weekly_km.shape)  ## Şekil yapısı     /   (3,3)
print(weekly_km.size)   ## Toplam parametre sayısı  /   9
print(weekly_km[0,:])   ## İlk haftanın tüm parametreleri   /   [5,8,10]
print(weekly_km[1,2])   ## ikinci haftanın 3. parametresi   /   12
print(weekly_km[:,0])   ## Bütün haftaların ilk parametreleri   /   [5,6,4]
weekly_km[2,1] = 8      ## 3.haftanın 2. parametresi 8 olarak değişti
print(weekly_km)        ## [[ 5  8 10] [ 6  9 12]  [ 4  8 11]]

""" 
Matris Metotları
veriyi analiz etmek ve anlamlı sonuçlar çıkarmak için matris metotları kullanılır.

1- reshape(satirSayisi,sutunSayisi)    -> Matrisin Şeklini değiştirir. Bir dizinin elemanlarını değiştirmeden farklı bir boyut yapısında düzenlemei sağlar. Eleman sayısı korunmalıdır aksi taktirde hata verecektir.

2- T    -> Matrisin transpozunu alır. Yani satırları sütunlara, sütunları satırlara dönüştürür. T aslında bir metot değil NumPy dizisinin bir özelliğidir.

3- sum()    -> Bir matrisin tüm elemanlarını toplamını hesaplar.
               axis=0 parametresi -> Her sütunun toplamını verir.
               axix=1 parametresi -> Her satırın toplamını verir.

4- mean()   -> Bir dizinin veya matrisin aritmetik ortalamasını hesaplar.
               axis=0 parametresi -> Her sütunun ortalamasını verir.
               axix=1 parametresi -> Her satırın ortalamasını verir.

5- min() ve max()   -> Bir dizinin ya da matris'in içindeki en küçük ve en büyük değeri verir.
                       axis=0 parametresi -> Her sütunun en küçük ve/veya en büyük değerini verir.
                       axix=1 parametresi -> Her satırın en küçük ve/veya en büyük değerini verir.

6- flatten()    -> İki boyutlu bir matrisi tek oyutlu bir diziye dönüştürmek için kullanılır.

"""

## reshape()
numbers = np.array([1,2,3,4,5,6,7,8,9])
matrixNumbers = numbers.reshape(3,3)    ## 3 satır 3 sütunlu olacak şekilde 2 boyutlu yapıya döndürür.
print(matrixNumbers)


## T    -> Transpoz alma

matrixData = np.array([
    [1,2,3],
    [4,5,6]
])

print(matrixData.T)             ## Satırlar ile sütunlar yer değiştirdi. Transpoz'dan sonra 2 satır 3 sütunlu yapı, 3 satır 2 sütunlu yapıya döndü

## sum()
print(matrixData.sum())         ## Ekrana 21 yazar.
print(matrixData.sum(axis=0))   ## Sütunların toplamı [5 7 9] sonucunu yazar.
print(matrixData.sum(axis=1))   ## Satırların toplamı [ 6 15] sonucunu yazar.

## mean()
print(matrixData.mean())        ## Ekrana 3.5 yazar
print(matrixData.mean(axis=0))  ## Ekrana [2.5 3.5 4.5] yazar.
print(matrixData.mean(axis=1))  ## Ekrana [ 2. 5.] yazar.

## min() ve max()
print(matrixData.min())         ## Ekrana 1 yazar.
print(matrixData.max())         ## Ekrana 6 yazar.
print(matrixData.min(axis=0))   ## Ekrana [1 2 3] yazar.
print(matrixData.max(axis=1))   ## Ekrana [3 6] yazar.
print(matrixData.min(axis=1))   ## Ekrana [1 4] yazar.
print(matrixData.max(axis=0))   ## Ekrana [4 5 6] yazar.

## flatten()

kosu = np.array([
    [350,400,450],
    [300,250,200],
    [500,550,600]
])

print(kosu.flatten())

""" 
Örnek - Mini Uygulama

1. Matrisin tüm elemanlarının toplamını bul. `sum()` kullan.
2. Her sütunun toplamını hesapla. `axis=0` kullan.
3. Her haftanın ortalama antrenman mesafesini bul. `mean()` ve `axis=1` kullan.
4. Matrisin transpozunu yazdır. `T` özelliğini kullan.
5. Matrisi 1 satır ve 9 sütundan oluşan bir yapıya dönüştür. `reshape(1, 9)` kullan.
6. Matrisin en büyük değerini bul.
"""
weekly_km = np.array([
    [5,8,9],
    [6,9,12],
    [4,7,11]
])

print(weekly_km.sum())          ## 71
print(weekly_km.sum(axis=0))    ## [15 24 32]
print(weekly_km.mean(axis=1))   ## [7.3 9. 7.3]
print(weekly_km.T)              ## [[5,6,4] [8,9,7] [9,12,11]]
print(weekly_km.reshape(1,9))   ## [5,8,9,6,9,12,4,7,11]
print(weekly_km.max())          ## 12

""" 
NumPy Vektör Metotları

Önceki metotlara ek olarak 
.argmin()   -> En küçük değerin indeksini verir.
.argmax()   -> En büyük değerin indeksini verir.

Not: İndeksi bilindiğinde, o değerin hangi konumda olduğu bulunabilir veya başka bir dizide aynı konumdaki veriye ulaşılabilir.
"""

kosuPace = np.array([300, 315, 290, 305, 310])
print(kosuPace.argmin())    ## 290 değerinin indisNo'su 2 yazar.
print(kosuPace.argmax())    ## 315 değerinin indisNo'su 1 yazar.


## Örnek - Mini Uygulama
# En hızlı bölümün pace değerini, argmin() ile bulduğun indeksi kullanarak yazdır.
# En yavaş bölümün pace değerini, argmax() ile bulduğun indeksi kullanarak yazdır.
# paces dizisindeki değerleri küçükten büyüğe sıralamak için np.sort() kullan.

paces = np.array([320,310,305,295,285])

print(paces[paces.argmin()])    ## 285 değerini indis 4 ile bulur ve ekrana 285 yazar.
print(paces[paces.argmax()])    ## 320 değerini indis 0 ile bulur ve ekrana 320 yazar.
print(np.sort(paces))           ## [285 295 305 310 320]
print(paces.mean())             ## Ekrana 303.0 yazar
print(paces.min())              ## Ekrana 285 yazar
print(paces.max())              ## Ekrana 320 yazar
print(paces.sum())              ## Ekrana 1515 yazar


""" 
NumPy Matrislerinde Dört İşlem
Toplama(+), Çıkarma(-), Bölme(/), Çarpma(*)
Not: Aynı konumdaki elemanlar ile dört işlemi gerçekleştirir.
"""

week1 = np.array([
    [5,8,10],
    [6,9,12]
])

week2 = np.array([
    [3,4,5],
    [2,3,4]
])

## TOPLAMA (+)
print(week1 + week2)
print(week1 + 2)        ## Her bir parametreyi 2 ile toplar

## ÇIKARMA (-)
print(week1 - week2)

## ÇARPMA (*)
print(week1 * week2)

## BÖLME (/)
print(week1 / week2)

## Örnek - Mini Uygulama
# A + B = ?
# A - B = ?
# A * B = ?
# A / B = ?
# A + 5 = ?
# B * 3 = ?
# A ve B matrislerini kullanarak eleman bazlı çarpım sonucunu result isimli bir değişkene ata ve yazdır.
# A matrisindeki bütün değerleri 2 ile böl ve sonucu yazdır.
# A matrisinden B matrisini çıkar, ardından ortaya çıkan matrisin toplamını sum() ile hesapla.

A = np.array([
    [10,20,30],
    [40,50,60]
])

B = np.array([
    [2,4,5],
    [8,10,12]
])

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A + 5)
print(B * 3)

result = A * B
print(result)
print(A/2)
C = A - B
print(C.sum())

""" 
NumPy Matrislerinde Filtreleme
Verilerin içinden yalnızca istenilen değerleri almak için kullanılır.


Operatör	    Anlamı	                Örnek
>	            Büyüktür	            weekly_km > 9
<	            Küçüktür	            weekly_km < 6
>=	            Büyük veya eşittir	    weekly_km >= 9
<=	            Küçük veya eşittir	    weekly_km <= 5
==	            Eşittir	                weekly_km == 10
!=	            Eşit değildir	        weekly_km != 10
"""

## 1- Koşullu Filtreleme ##
## Ör: 9km'den daha büyük değerleri bulma
weekly_km = np.array([
    [5,8,10],
    [6,9,12],
    [4,7,11]
])

print(weekly_km > 9)

""" 
[[False False  True]
 [False False  True]
 [False False  True]]

 response döner.
 NumPy her parametreyi tek tek kontrol eder 9'dan büyük olan değerler true 9'a eşik ve küçük olan değerlere false ataması yapar.

 Ancak bu hangi değerin koşulu sağladığını gösterir. Gerçek değeri almak için filtreyi doğrudan diziye uygularız.
"""

print(weekly_km[weekly_km>9])   ## Ekrana [10 12 11] yazar.

## Ör: 6km'den az olan değerleri yazdırın
print(weekly_km[weekly_km<6])   ## Ekrana [5 4] yazar.


## 2- Birden fazla koşulu birleştirmek
# Gerçek veri analizinde çoğu zaman tek bir koşul yeterli olmaz.
# Örneğin, "6 veya daha fazla" ve "10 veya daha az" kilometre olan değerleri seçmek isteyebiliriz.
# Örneğin "5'ten Küçük" veya "10'dan Büyük" kilometre olan değerleri seçmek isteyebiliriz.
# NumPy'de birden fazla koşul için & (ve) ve | (veya) operatörlerini kullanırız.
# Önemli: Birden fazla koşul kullanırken her koşulu paranteze alınmalı.

print(weekly_km[(weekly_km >= 6) & (weekly_km <= 10)])     ## Ekrana [ 8 10  6  9  7] yazar.
print(weekly_km[(weekly_km < 5) | (weekly_km > 10)])       ## Ekrana [12 4 11] yazar.


## Filtrelenen değeri değiştirmek
## İstersek filtrelenen veriyi değiştirebiliriz.

weekly_km[weekly_km > 10] = 10
print(weekly_km)

### Örnek - Mini Uygulama ###
# 8'den büyük değerleri filtrele.
# 5'ten küçük veya 10'a eşit değerleri filtrele. 
# 6 veya daha büyük ve 10 veya daha küçük değerleri filtrele.
# 12 değerinin bulunduğu konumu True olarak yazdır.
# 10'dan büyük değerleri 10 olarak değiştir ve matrisi yazdır.

weekly_km = np.array([
    [5, 8, 10],
    [6, 9, 12],
    [4, 7, 11]
])

print(weekly_km[weekly_km > 8])
print(weekly_km[(weekly_km < 5) | (weekly_km == 10)])
print(weekly_km[(weekly_km >= 6) & (weekly_km<=10)])
print(weekly_km == 12)

weekly_km[weekly_km>10] = 10
print(weekly_km)


""" 
NumPy Matrislerinde Birleştirme


Birbirinden farklı NumPy Dizi ve vektörlerini birleştirme için kullanılır.
.concatenate()
.vstack()
.hstack()
"""

## Örneğin iki farklı matrislerini birleştirme

week1 = np.array([
    [5,8,10],
    [6,9,12]
])

week2 = np.array([
    [4,7,11],
    [5,8,10]
])


""" 
np.concatenate()     bu metot ile belirtilecek eksen yönünde diziler birleştirilir.
İki matrisi satır ve sütun yönünde birleştirme    -> axis=0 ve axis=1
Önemli kural: concatenate() kullanırken birleştirme yaptığın eksen dışındaki boyutların aynı olması gerekir.
- axis=0: Sütun sayıları eşit olmalı.
- axis=1: Satır sayıları eşit olmalı.
"""

result = np.concatenate((week1,week2), axis=0)
print(result)

""" 
[[ 5  8 10]
 [ 6  9 12]
 [ 4  7 11]
 [ 5  8 10]]
"""


result = np.concatenate((week1,week2), axis=1)
print(result)

""" 
[[ 5  8 10  4  7 11]
 [ 6  9 12  5  8 10]]
"""


#### np.vstack() Dikey Birleştirme ve np.hstack() yatay birleştirme

vresult = np.vstack((week1,week2))
print(vresult)

"""
Sonuç axis=0 ile aynıdır.

[[ 5  8 10]
 [ 6  9 12]
 [ 4  7 11]
 [ 5  8 10]]
"""

hresult = np.hstack((week1,week2))
print(hresult)

""" 
Sonuç axis=1 ile aynıdır.

[[ 5  8 10  4  7 11]
 [ 6  9 12  5  8 10]]
"""

## Not: vstack() ve hstack() farklı boyutlu dizilerde de kullanılabilir; ancak boyutların birleştirme işlemine uygun olması gerekir.


## Örnek - Mini Uygulama
# np.concatenate() kullanarak iki matrisi alt alta birleştir.
# np.concatenate() kullanarak iki matrisi yan yana birleştir.
# np.vstack() ile iki matrisi birleştir.
# np.hstack() ile iki matrisi birleştir.
# Dört sonucun da shape değerini yazdır.


week1 = np.array([
    [5, 8],
    [6, 9]
])

week2 = np.array([
    [10, 12],
    [11, 13]
])


result1 = np.concatenate((week1,week2), axis=0)
result2 = np.concatenate((week1,week2), axis=1)
result3 = np.vstack((week1,week2))
result4 = np.hstack((week1,week2))

print(result1)
print(result2)
print(result3)
print(result4)
print(np.shape(result1))
print(np.shape(result2))
print(np.shape(result3))
print(np.shape(result4))

##### NumPy Matris Oluşturma Metotları konusundan devam et ######