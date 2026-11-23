import pandas as pd         ## Pandas kütüphanesini yükler
import sqlite3              ## sqlite kütüphanesini yükler
import os                   ## Dosya işlemlerim kütüphanesini yükler

""" 
Data Preprocessing (Veri Ön İşleme)

Data Preprocessing, ham verilerin analiz veya makine öğrenmesi için hazırlanması sürecidir.

Gerçek hayatta veriler çoğunlukla doğrudan analize uygun değildir. Örneğin bir e-ticaret veri tabanında:
- Müşterinin telefon numarası eksik olabilir.
- Sipariş tarihi boş olabilir.
- Aynı sipariş kaydı iki kez bulunabilir.
- Ürün fiyatı yanlışlıkla 0 girilmiş olabilir.
- Bir sütunda tarih yerine metin bulunabilir.
- Kategoriler farklı yazımlarla kaydedilmiş olabilir.
Bu tür sorunlar analiz sonuçlarını yanıltabilir.

Örnek: Bir e-ticaret şirketinin ortalama sipariş tutarı hepsalanıyor. Fiyat alanında hatalı veya eksik kayıtlar varsa hesaplanan ortalama gerçeği yansıtmayabilir.

Veri Ön İşlemenin Temel Aşamaları

İşlem	                            Açıklama
Eksik verileri tespit etme	        Boş hücreleri bulma
Eksik verileri yönetme	            Silme veya uygun değerle doldurma
Tekrarlanan kayıtları bulma	        Duplicate kayıtları tespit etme
Tekrarlanan kayıtları temizleme	    Gereksiz tekrarları kaldırma
Veri tiplerini kontrol etme	        Yanlış veri tiplerini düzeltme
Hatalı verileri tespit etme	        Mantıksız veya geçersiz değerleri bulma
Metin verilerini temizleme	        Boşluk, yazım ve biçim farklılıklarını düzenleme

"""


### EKSİK VERİLERİ TESPİT ETME (MISSING VALUES) ####

""" 
Pandas'ta eksik veriler genellikle Nan veya None olarak temsil edilir.

-   .isnull()   -> Bir hücrenin boş olup olmadığını kontrol eder.   Hücre boş ise True, dolu ise False sonucunu döner.
-   .notnull()  -> Bir hücrenin dolu olup olmadığını kontrol eder.  Hücre dolu ise True, boş ise False sonucunu döner. 
-   .isnull().sum() -> Önemli bir kullanımdır. Her sütunda kaç adet eksik değer olduğunu hesaplar.
-   .isnull().sum().sum()   -> Bütün DataFrame içerisindeki toplam eksik hücre sayısını verir.

"""


sqlFile = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

dbPath = os.path.join(
    sqlFile,
    'olist_dataset.db'
)

baglan = sqlite3.connect(dbPath)

df_orders = pd.read_sql('select * from orders',baglan)

print(df_orders.isnull().sum())         ## Sütunlardaki Boş hücrelerin sayısını verir.
print(df_orders.notnull().sum())        ## Sütunlardaki Dolu hücrelerin sayısını verir.

print(f'Toplam boş hücre sayısı: {df_orders.isnull().sum().sum()}')
print(f'Toplam Dolu Hücre Sayısı: {df_orders.notnull().sum().sum()}')

eksik_veriler_satir = df_orders[df_orders.isnull().any(axis=1)]       ## Satırlara göre boşlukları bulur ver indisNo'ya göre listeler
print(eksik_veriler_satir)


""" 
Mini Uygulama
1- orders tablosunu df_orders isimli DataFrame'e aktar.
2- Her sütundaki eksik değer sayısını bul.
3- Tüm tablodaki toplam eksik hücre sayısını bul.
4- En az bir eksik değeri bulunan ilk 20 kaydı ekrana getir.
"""

sqlFile = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

dbPath = os.path.join(
    sqlFile,
    'olist_dataset.db'
)

baglan = sqlite3.connect(dbPath)

df_orders = pd.read_sql('select * from orders',baglan)

print(df_orders.isnull().sum())
print(df_orders.isnull().sum().sum())

eksik_veriler = df_orders[df_orders.isnull().any(axis=1)]
print(eksik_veriler.head(20))


#### EKSİK VERİLERİ YÖNETME ####

""" 
-   .dropna()   -> Eksik değeri bulunan satırları kaldırır.
-   .fillna()   -> Eksik verileri doldurmak için kullanılır. Eksik hücreler sıfır ile doldurulur.


Ancak dikkat: Her eksik değeri silmek veya sıfırla doldurmak doğru değildir. Karar verirken sütunun neyi temsil ettiğini anlamamız gerekir.

Örneğin Olist verimizde order_delivered_customer_date alanının boş olması, siparişin henüz müşteriye teslim edilmediği anlamına gelebilir. Bu bilgiyi silmek istemeyiz.

Önemli bir ayrıntı: Her eksik veri aynı anlama gelmez

Örneğin Olist verimizden:
Sütun	                        Eksik olmasının olası anlamı
order_approved_at	            Sipariş henüz onaylanmamış olabilir.
order_delivered_carrier_date	Kargo henüz taşıyıcıya teslim edilmemiş olabilir.
order_delivered_customer_date	Sipariş müşteriye henüz ulaşmamış olabilir.

Dolayısıyla eksik değerleri silmek veya sıfırla doldurmak yerine önce neden eksik olduklarını bilmek önemlidir.
"""

df_silinen = df_orders.dropna()
print(df_silinen)

df_doldurulan = df_orders.fillna(0)
print(df_doldurulan)

print(f'Orijinal: {df_orders.isnull().sum().sum()}')
print(f'Silinen: {df_silinen.isnull().sum().sum()}')
print(f'Doldurulan: {df_doldurulan.isnull().sum().sum()}')


#### Tekrarlanan Kayıtlar ####

""" 
Örneğin bir e-ticaret projesine bir siparişin veya bir müşteri kaydının birden fazla kayıt edilidiğini düşünelim.

-   .duplicated()           -> Tekrar eden kayıtları tespit etmek için kullanılır.
-   .drop_duplicates()      -> Varsayılan olarak ilk karşılaşılan kayıt korunucak şekilde mükerrer kayıtlar silinir.
-   subset=['sütun adı']    -> Sütuna göre tekrar kontrolü yapmak
-   astype()                -> Bir sütunun veri tipini dönüştürme
-   pd.to_datetime()        -> Tarih olarak saklanan metinleri Pandas veri tipine dönüştürür.
"""

print(f'Tekrarlanan Data: {df_orders.duplicated().sum()}')      ## Tekrarlanan Data Saysını Verir.

tekrarlar = df_orders[df_orders.duplicated()]
print(tekrarlar)                            

df_tekrarsiz = df_orders.drop_duplicates()                      ## Varsayılan olarak ilk karşılaşılan kayıt korunucak şekilde mükerrer kayıtlar silinir.
print(df_tekrarsiz)

musteriNo = df_orders.duplicated(subset=['customer_id']).sum()
print(musteriNo)


### Müşteri Id'lerini Listeme
print(df_orders['customer_id'].head(20))

### Benzersiz Müşteri Sayısı
print(df_orders['customer_id'].unique())

### Toplam Sipariş Sayısı
print(df_orders['order_id'].count())

### En çok siperiş veren müşteri
print(df_orders['customer_id'].value_counts().head(10))

## Sütunların veri tiplerini incleme
print(df_orders.dtypes)

## Spesifik bir sütunun veri tipini inceleme
print(df_orders['order_purchase_timestamp'].dtype)

## Veri tipi dönüştürme
# df_orders['customer_id'] = df_orders['customer_id'].astype('Int64')
# print(df_orders.dtypes)

## Pandas veri tarihine dönüştürme
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders['order_delivered_carrier_date'] = pd.to_datetime(df_orders['order_delivered_carrier_date'])
df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'])
df_orders['order_estimated_delivery_date'] = pd.to_datetime(df_orders['order_estimated_delivery_date'])
df_orders['order_approved_at'] = pd.to_datetime(df_orders['order_approved_at'])

print(df_orders.dtypes)