""" 
PANDAS

- Pandas, bu tip tablo verilerini Python içinde kolayca yönetmeyi ve analiz etmeyi sağlayan bir kütüphanedir. CSV, Excel ve SQL gibi kaynaklardan veri okuyabilir; veriyi inceleyebilir, temizleyebilir, hesaplayabilir ve sonuçları dışarı aktarabilir.

Çalışma Şekli
Ham Veri (CSV, Excel, SQL) -> Pandas DataFrame (Veriyi düzenle, incele, temizle) -> Analiz ve Rapor (Hesaplamalar · Filtreler · İş kararları)

Örneğin satış dosyasındaki her sipariş için adet × birim fiyat hesabını yapabilir, ardından kategori bazında gelirleri karşılaştırabilir. Böylece yalnızca veriyi göstermekle kalmaz, veriden anlamlı sonuçlar da çıkarılabilir.

- Pandas kütüphanesi projeye import edilmelidir.
import pandas as pd

"""

import pandas as pd

""" 
PANDAS Veri Türleri

Pandas'ta veri türlerini bilmek, kontrol etmek önemlidir. Analiz edilecek değerler üzerinde yapılacak işlemlerde hata almamak adına dtype metodu ile kontroller yapılır.
"""

adetler = pd.Series([2,3,1])
fiyatlar = pd.Series([750.50,400.00,5200.00])
urunler = pd.Series(['Klavye', 'Mouse', 'Monitör'])
odemeler = pd.Series([True,False,True])

print(adetler.dtype)
print(fiyatlar.dtype)
print(urunler.dtype)
print(odemeler.dtype)

miktar = pd.Series(['100','200','300'])
print(miktar.dtype)     ## Ekrana str olarak döner

miktar = pd.Series(['100','200',300])
print(miktar.dtype)     ## Ekrana object olarak döner


## Örneğin bir data içinde Numerik değerler tırnak içinde olduğunu düşünelim. Bu değerlerin int64 veri tipine dönüştürmek için pd.to_numeric(degisken ya da parametre) metodu kullanılır.

print(pd.to_numeric(miktar))

## Örneğin data içinde str sayı ve str metin var. Bunların veri türünü dönüştürmek istediğimizde hata oluşacaktır. Bu sebeple dönüştürme yaparken erros="coerce" parametresi kullanılırsa hatalı olan veri NaN olarak değerlendirilir ve kod çalışmaya devam eder.

info = pd.Series(['100','200',"hatalı",'300'])
print(pd.to_numeric(info, errors='coerce'))


""" 
Pandas DataFrame

DataFrame, verileri satırlar ve sütunlar halinde saklayan iki boyutlu bir veri yapısıdır. Excel tablosu veya veritabanındaki bir tablo gibi düşünülebilir.

Örneğin, bir e-ticaret şirketinin sipariş verileri:

Ürün	    Adet	    Birim Fiyat
Klavye	    2	        750.50
Mouse	    3	        400.00
Monitör	    1	        5200.00

Bu tablonun tamamı bir DataFrame olabilir.

- Satır (row): Bir sipariş kaydını temsil eder.
- Sütun (column): Ürün, adet veya fiyat gibi bir özelliği temsil eder.
- Hücre (cell): Bir satırla sütunun kesişimindeki tek bir değerdir.

Gerçek bir projede ne işe yarar?
Diyelim ki şirkete ait 50.000 sipariş içeren bir dosya mevcut ve şu soruların yanıtları isteniyor:

- Hangi ürün en çok satılmış?
- Toplam satış tutarı ne kadar?
- Hangi ürünlerin fiyatı 1.000 TL'den fazla?
- Hangi ödeme durumundaki siparişler tamamlanmamış?

DataFrame, bu verileri düzenli biçimde tutmayı ve sonraki aşamalarda filtreleme, hesaplama ve analiz yapmayı sağlar.


DataFrame ile Series arasındaki ilişki
Bir DataFrame'i bir Excel tablosunun tamamı, Series'i ise o tablonun tek bir sütunu gibi düşünülebilir.
"""

##### DataFrame Oluşturma #####
## sözlük(dictionary) yapısını DataFrame içine verme.
## pd.DataFrame(degisken ya da parametre) -> İlgili veriyi tablo haline dönüştürür.
## Önemli Not: dataların uzunlukları eşit olmalıdır aksi taktirde hata verecektir.

veriler = {
    "Ürün" : ["Klavye","Mouse","Monitör"],
    "Adet": [2,3,1],
    "Birim Fiyat" : [750.50, 400.00, 5200.00]
}

df = pd.DataFrame(veriler)      ## Dictionary yapısındaki datayı DataFrame ile tabloya dönüştürdü.
print(df)                       ## Data tablo halinde görünür.


""" 
**** ÖRNEK ****

Bir çevrim içi kitap mağazasında şu veriler bulunuyor:
- Kitap: "Python", "SQL", "Excel"
- Stok: 10, 5, 8
- Fiyat: 350, 250, 180

Veriler adında bir sözlük oluşturun, ardından bunu df adlı bir DataFrame'e dönüştürüp ve tabloyu ekrana yazdırın.
"""

veriler = {
    "Kitap":["Python","SQL","Excel"],
    "Stok":[10,5,8],
    "Fiyat":[350,250,180]
}

df = pd.DataFrame(veriler)

print(df)


############## Pandas Serileri (Series) ##############
## Series, Pandas'ın tek boyutlu veri yapısıdır. Değerleri ve bu değerlere karşılık gelen indeksleri içerir.
## Bir listeyi(dizi datayı) pd.Series() içine vererek Series oluşturabilir.

stoklar = pd.Series([10,5,8])
print(stoklar)
print(stoklar.sum())    ## Toplam stok miktarı
print(stoklar.mean())   ## Ortalama stok miktarı


## Örnek
## Bir kitap mağazasının satış verileri şöyle 12,7,15,4
## Bu verilerden bir Series oluşturup toplam satış adedini ekrana yazdırın.

satislar = pd.Series([12,7,15,4])
print(satislar)
print(satislar.sum())


### Pandas'ta Index ve Columns ###

veriler = {
    "Kitap": ["Python", "SQL", "Excel"],
    "Stok": [10, 5, 8],
    "Fiyat": [350, 250, 180]
}

df = pd.DataFrame(veriler)
print(df)

print(df.index)
print(df.columns)

## Kolon isimlerini güncelleme
dfr = df.rename(columns={'Fiyat':'Birim Fiyat'})
print(dfr)

## Index bilgisi güncelleme
dfr.index = ['urun-01','urun-02','urun-03']
print(dfr)



### ÖRNEK
### Sütun adlarını ekrana yazdırın
### Satır indekslerini ekrana yazdırın
### Fiyat sütununun adını Birim Fiyat olarak değiştirin
### Yeni sütun adlarını tekrar ekrana yazdır

veriler = {
    'Kitap':['Python','SQL','Excel'],
    'Stok':[10,5,8],
    'Fiyat':[350,250,180]
}

df = pd.DataFrame(veriler)
print(df)

print(df.columns)
print(df.index)
print(df.rename(columns={'Fiyat':'Birim Fiyat'}))
print(df.columns)

""" 
#### Pandas Metotları ####

-   .head() -> Varsayılan haliyle ilk 5 satırı getirir. Parametre parantezine sayı verilirse istenilen sayıda ilk satırlar görüntülenebilir.
-   .tail() -> Varsayılan haliyle son 5 satırı getirir. Parametre parantezine sayı verilirse istenilen sayıda son satırlar görüntülenebilir.
-   .describe() -> Sayısal sütunlar için adet, ortalama, standart sapma, minimum, çeyrekler ve maksimum gibi istatistikleri gösterir.
-   .info() -> Satır sayısını, sütunları, veri tiplerini ve dolu değer sayılarını gösterir. Eksik verileri araştırırken çok işe yarar.
-   .sum()  -> Seçilen sütunun toplamını hesaplar. Series üzerinde kullandığımız metotların DataFrame sütunlarında da uygulanmasına örnektir.
        Ör: df["Adet"].sum()    -> Adet sütunun toplamı
-   .mean() -> Seçilen sütunun ortalamasını hesaplar. Series üzerinde kullandığımız metotların DataFrame sütunlarında da uygulanmasına örnektir.
        Ör: df["Fiyat"].mean()  -> Fiyat sütunun ortalaması

"""

veriler = {
    "Urun": ["Klavye", "Mouse", "Monitör", "Kulaklık", "Webcam", "HarDisk"],
    "Adet": [12, 25, 8, 15, 10, 20],
    "Fiyat": [750, 400, 5200, 1250, 1800, 2000]
}

df = pd.DataFrame(veriler)

print(df.head())        # Varsayılan olarak ilk 5 kaydı verir.
print(df.tail())        # Varsayılan olarak son 5 kaydı verir.
print(df.tail(2))       # parametre olarak 2 değeri gildiği için son 2 kaydı verir.


""" 
### Örnek - Mini Uygulama ###
Yukarıdaki df tablosunu oluşturduğunu varsay. Şimdi şu üç görevi yerine getirecek kodu yaz:
- İlk 3 ürünü göster.
- Veri setinin yapısını ve sütun bilgilerini kontrol et.
- Ürünlerin toplam stok miktarını hesapla.
"""
print('**** Mini Uygulama 1 ****')
print(df.head(3))       # parametre olarak 3 değeri gildiği için ilk 3 kaydı verir.
print(df.info())
print(df['Adet'].sum())



""" 
### Series Metotları ###

-   .sum()  -> Bütün satış adetlerini toplar.
-   .mean() -> Satışların aritmetik ortalamasını hesaplar.
-   .max() ve .min()    -> En yüksek ve en düşük satış miktarlarını bulur.
-   .count()    -> Dolu değer sayısı. Eksik olmayan değerlerin sayısını verir.
-   .value_counts() -> Değerlerin tekrar sayısı. Her değerin kaç kez tekrarlandığını gösterir.
-   .unique()   ->  Benzersiz değerler. Tekrarlanan değerleri bir kez gösterir.
-   .nunique()  ->  Benzersiz değer sayısı. Kaç farklı değer bulunduğunu sayar.
"""


siparisler = pd.Series([5,8,5,12,8,5,15,12,20,8])

""" 
Örnek - Mini uygulama 2

1- Toplam sipariş adedini hesaplayın.
2- Günlük ortalama sipariş miktarını hesaplayın.
3- En yüksek sipariş miktarını bulun.
4- Kaç farklı sipariş miktarı olduğunu bulun.
5- Hangi sipariş miktarının kaç kez tekrarlandığını gösterin.
"""
print('*** Mini Uygulama 2***')
print(siparisler.sum())
print(siparisler.mean())
print(siparisler.max())
print(siparisler.unique())
print(siparisler.nunique())
print(siparisler.value_counts())


""" 
#### DataFrame Metotları ####

-   .shape      -> Tablo boyutunu verir. Ör:(6,5) yani 6 satır 5 sütun. Not: Bu bir metot değil bir DataFrame özelliğidir. Bu yüzden parantezi yoktur.
-   .columns    -> Sütun isimlerini verir. Not: Bu bir metot değil bir DataFrame özelliğidir. Bu yüzden parantezi yoktur.
-   .dtypes     -> Sütunların veri tiplerini verir. Not: Bu bir metot değil bir DataFrame özelliğidir. Bu yüzden parantezi yoktur.
-   .info()     -> Tablo hakkında genel bir bilgi verir. Satır sayısı, sütun sayısı, veri tipleri ve boş olmayan değer sayıları gibi bilgileri verir.

"""

veriler = {
    "Urun": ["Laptop", "Mouse", "Klavye", "Monitor", "Kulaklik", "Webcam"],
    "Kategori": ["Bilgisayar", "Aksesuar", "Aksesuar", "Bilgisayar", "Aksesuar", "Aksesuar"],
    "Stok": [12, 35, 20, 8, 15, 10],
    "Fiyat": [25000, 750, 1200, 8500, 1800, 2200],
    "Satis": [8, 25, 12, 5, 10, 7]
}

df = pd.DataFrame(veriler)

print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())