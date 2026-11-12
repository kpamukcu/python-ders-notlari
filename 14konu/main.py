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
-   .describe() -> Sayısal verilerin istatiksel özeti
-   .sum()      -> Sütunların toplamı
-   .mean()     -> Sütunların ortalaması
-   .value_counts() -> Değerlerin tekrar sayısı. data üzerinden belirli bir sütun çekilerek kullanılır.


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
print(df.describe())
print(df.sum(numeric_only=True))    ## numeric_only=True sadece sayılsal değerlerin toplamını verir.
print(df['Kategori'].value_counts())


""" 
Örnek - Mini Uygulama
veriler = {
    "Urun": ["Laptop", "Mouse", "Klavye", "Monitor", "Kulaklik", "Webcam"],
    "Kategori": ["Bilgisayar", "Aksesuar", "Aksesuar", "Bilgisayar", "Aksesuar", "Aksesuar"],
    "Stok": [12, 35, 20, 8, 15, 10],
    "Fiyat": [25000, 750, 1200, 8500, 1800, 2200],
    "Satis": [8, 25, 12, 5, 10, 7]
}

Ürün envanteri raporu

Şirket yöneticisi ürün envanteri hakkında bir rapor istiyor.

Aşağıdaki işlemleri yap:
1. Tablo kaç satır ve kaç sütundan oluşuyor?
2. Sütun isimlerini ekrana yazdır.
3. Veri tiplerini göster.
4. DataFrame'in genel bilgilerini göster.
5. Sayısal sütunların istatistiksel özetini çıkar.
6. Toplam stok miktarını hesapla.
7. Ürünlerin ortalama satış miktarını hesapla.
8. Kategorilerde kaç ürün bulunduğunu göster.
"""



""" 
DataFrame Fİltreleme İşlemleri 

Filtreleme -> Bir DataFrame içerisindeki belirli koşulları sağlayan satırları seçme işlemidir.
Ör: Stok miktarı 10'un altındaki ürünlerin listesi
"""

## TEK KOŞULLU FİLTRELEME

veriler = {
    "Urun": ["Laptop", "Mouse", "Klavye", "Monitor", "Kulaklik", "Webcam"],
    "Kategori": ["Bilgisayar", "Aksesuar", "Aksesuar", "Bilgisayar", "Aksesuar", "Aksesuar"],
    "Stok": [12, 35, 20, 8, 15, 10],
    "Fiyat": [25000, 750, 1200, 8500, 1800, 2200],
    "Satis": [8, 25, 12, 5, 10, 7]
}

df = pd.DataFrame(veriler)

## Ör: Stok miktarı 10'un altındaki ürünlerin listesi
sonuc = df[df['Stok']<10]
print(sonuc)                ## 3  Monitor  Bilgisayar     8   8500      5


## BİRDEN FAZLA KOŞUL KULLANMAK
## Önemli: Birden fazla koşul kullanırken her koşulu parantez içine alınmalıdır.

## ÖR: "Stok miktarı 10'dan fazla VE fiyatı 1.000 TL'den yüksek ürünleri listele."

sonuc = df[(df['Stok']>10) & (df['Fiyat']>1000)]
print(sonuc)

### 4. Belirli değerleri filtrelemek ###
sonuc = df[df['Kategori'] == 'Bilgisayar']                      ## Kategorisi Bilgisayar olan
print(sonuc)

## Birden fazla değere göre filtreleme
sonuc = df[df['Kategori'].isin(['Aksesuar','Bilgisayar'])]      ## Kategorisi Aksesuar ve Bilgisayar olan
print(sonuc)

""" 
Örnek - Mini Uygulama
E-ticaret şirketinin ürün yöneticisi senden üç ayrı rapor istiyor.

Görev 1: Fiyatı 2.000 TL'den yüksek olan ürünleri listele.
Görev 2: Stok miktarı 10 veya daha az olan ürünleri listele.
Görev 3: Kategorisi Aksesuar olan VE stok miktarı 10'dan fazla olan ürünleri listele.

Her görev için ayrı bir filtreleme işlemi yaz.
"""
print('**** Filtreleme Mini Uygulama Sonuçları ****')
gorev1 = df[df['Fiyat']>2000]               ## Alternatif kullanım: df.query('Fiyat > 2000')
print(gorev1)

gorev2 = df[df['Stok']<=10]                 ## Alternatif kullanım: df.query('Stok <=10')
print(gorev2)

gorev3= df[(df["Kategori"]=='Aksesuar') & (df["Stok"]>10)]      ## Alternatif kullanım: df.query('Kategori == "Aksesuar" & Stok > 10')
print(gorev3)


""" 
Örnek - Mini Uygulama
İstenen rapor: Kategorisi Bilgisayar olan VE fiyatı 5.000 TL'den yüksek ürünleri listele.
1. Klasik DataFrame filtreleme yöntemiyle.
2. query() yöntemiyle.
"""

rapor1 = df[(df['Kategori'] == 'Bilgisayar') & (df["Fiyat"] > 5000)]
print(rapor1)

rapor2 = df.query("Kategori == 'Bilgisayar' and Fiyat > 5000")
print(rapor2)


""" 
Group İşlemleri (grouphy)
Verileri gruplandırarak analiz etmek için kullanılır. 
Ör: ürünleri kategorilerine göre gruplandırıp her kategorinin performansını incelemek.
    Bilgisayar kategorisinde kaç ürün var?
    Aksesuar kategorisindeki toplam stok miktarı nedir?
    Her kategorinin ortalama ürün fiyatı nedir?
    Kategorilere göre toplam satış miktarı nedir?

Bunları tek tek filtreleme yaparak hesaplamak yerine groupby() ile gerçekleştirebiliriz.
"""

veriler = {
    "Urun": ["Laptop", "Mouse", "Klavye", "Monitor", "Kulaklik", "Webcam"],
    "Kategori": ["Bilgisayar", "Aksesuar", "Aksesuar", "Bilgisayar", "Aksesuar", "Aksesuar"],
    "Stok": [12, 35, 20, 8, 15, 10],
    "Fiyat": [25000, 750, 1200, 8500, 1800, 2200],
    "Satis": [8, 25, 12, 5, 10, 7]
}

df = pd.DataFrame(veriler)

gruplar = df.groupby('Kategori')
print(gruplar)

stokAdetleri = df.groupby('Kategori')['Stok'].sum()        ## Kategorilere ayır, stok sütununu seç ve her kategoriye göre stok adetlerini topla
print(stokAdetleri)

toplamSatis = df.groupby('Kategori')['Satis'].sum()
print(toplamSatis)

ortalamaFiyat = df.groupby('Kategori')['Fiyat'].mean()
print(ortalamaFiyat)

urunSayisi = df.groupby('Kategori')['Urun'].count()         ## count(), ilgili sütundaki boş olmayan kayıtları sayar.
print(urunSayisi)


""" 
## Birden fazla hesaplama agg()

Örneğin her kategori için:
- Toplam stok
- Ortalama fiyat
- Toplam satış

değerini tek bir raporda göstermek.

"""

analizRaporu = df.groupby('Kategori').agg({
    "Stok": "sum",
    "Fiyat": "mean",
    "Satis": "sum"
})

print(analizRaporu)



""" 
Örnek - Mini Uygulama

E-ticaret şirketinin yöneticisi yeni bir rapor istiyor.

Aşağıdaki işlemleri gerçekleştirilecek :
1. Kategorilere göre toplam stok miktarını hesapla.
2. Kategorilere göre ortalama satış miktarını hesapla.
3. Kategorilere göre ürün sayısını hesapla.
4. agg() kullanarak tek bir tabloda şu üç bilgiyi göster:
   - Stok toplamı
   - Fiyat ortalaması
   - Satış toplamı
"""

rapor1 = df.groupby('Kategori')['Stok'].sum()
print(rapor1)

rapor2 = df.groupby('Kategori')['Satis'].mean()
print(rapor2)

rapor3 = df.groupby('Kategori')['Urun'].count()
print(rapor3)

rapor4 = df.groupby('Kategori').agg({
    'Stok':'sum',
    'Fiyat':'mean',
    'Satis': 'sum'
})
print(rapor4)


""" 
Örnek - Mini Uygulama 2
Her kategorideki ürünlerin toplam satış miktarını ve ortalama fiyatını tek bir DataFrame içerisinde göster. Kategori normal sütun olarak kalsın.

as_index=False kullanımı
"""

rapor5 = df.groupby('Kategori', as_index=False).agg({
    'Satis':'sum',
    'Fiyat':'mean'
})

print(rapor5)


""" 
Stack İşlemleri
DataFrame verilerinin satır ve sütun yapısını değiştirmeyi öğreneceğiz. Özellikle farklı raporlama ve veri analizi süreçlerinde kullanacağımız bir yöntem.
bir DataFrame'in sütunlarını çok seviyeli bir satır indeksine dönüştürür. Yani geniş tablo yapısını daha uzun bir yapıya dönüştürür.
"""

veriler = {
    "Kategori": ["Bilgisayar", "Aksesuar"],
    "Ocak": [100, 80],
    "Subat": [120, 90],
    "Mart": [150, 110]
}

df = pd.DataFrame(veriler)      ##Dict yapısı dataframe'e dönüştürüldü.
print(df)

df = df.set_index('Kategori')   ## Kategori sütunu index'e dönüştürüldü.
print(df)

sonuc = df.stack()              ## iki seviyeli bir index oluştu. sonuç artık bir DataFrame değil, bir Series.
print(sonuc)


"""
Stack sonucunu tekrar DataFrame yapma

.reset_index() metodu ile Series olan datayı tekrardan DataFrame formatına dönüştürürüz.
degiskenAdi.columns = ["Kategori", "Ay", "Satis"] ile sütunların isimlerini tekrar düzenleyebiliriz.
"""

sonuc = df.stack().reset_index()
print(sonuc)

sonuc.columns = ['Kategori','Ay','Satış']
print(sonuc)

""" 
Örnek - Mini Uygulama
veriler = {
    "Kategori": ["Bilgisayar", "Aksesuar", "Telefon"],
    "Ocak": [100, 80, 150],
    "Subat": [120, 90, 170],
    "Mart": [150, 110, 200]
}

Kategori sütununu index olarak ayarla.
stack() kullanarak ayları satır yapısına dönüştür.
Oluşan sonucu reset_index() ile DataFrame haline getir.
Sütun isimlerini Kategori, Ay, Satis olarak düzenle.

"""

veriler = {
    "Kategori": ["Bilgisayar", "Aksesuar", "Telefon"],
    "Ocak": [100, 80, 150],
    "Subat": [120, 90, 170],
    "Mart": [150, 110, 200]
}

df = pd.DataFrame(veriler)
df = df.set_index('Kategori')
df = df.stack()
df = df.reset_index()
df.columns = ['Kategori','Ay','Satis']
print(df)

import os
klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

dosyalar = os.listdir(klasor)
print(dosyalar)

""" 
#### CSV ile DataFrame oluşturma ####
CSV dosyalarını Python'da okuyabilmek için DataFrame'e dönüştürülür.

-   .read_csv()     ->  CSV dosyalarını okumayı sağlar.

.read_csv parametreleri ve görevleri
Parametre	        Görevi
sep                 Sütun ayırıcı karakteri belirler
encoding	        Karakter kodlamasını belirler
usecols	            Yalnızca istenen sütunları okur
nrows	            Okunacak satır sayısını sınırlar
index_col	        Hangi sütunun index olacağını belirler
parse_dates	        Belirtilen sütunları tarih formatında okumaya çalışır
"""

klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

df = pd.read_csv(klasor + r'\olist_orders_dataset.csv')
print(df)

print(df.head())    ## İlk 5 satırı varsayılan olarak getirir.
print(df.tail())    ## Son 5 satırır varsayılan olarak getirir.


### Belirli sütunları seçmek
df = pd.read_csv(
    klasor + r'\olist_orders_dataset.csv',
    usecols=['order_id','customer_id','order_status']       ## Belirlenen sütunları kullanacak
)

print(df.head())        ## olist_orders_dataset.csv datası içindeki ilk 5 kaydı sadece usecols'ta belirtilen sütunlar olacak şekilde getirir.


### Satır sayısını sınırlandırmak
df = pd.read_csv(
    klasor + r'\olist_orders_dataset.csv',
    nrows=100
)

print(df)