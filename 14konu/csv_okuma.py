import pandas as pd
import os

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
    nrows=100           ## İlk 100 datayı okur
)

print(df)


""" 
Örnek - Mini Uygulama
1- CSV dosyasını df değişkenine aktar.
2- İlk 10 siparişi göster.
3- Veri yapısını incele
    - Kaç satır ve sütun var?
    - Sütun isimleri neler?
    - Veri tipleri neler?
4- CSV dosyasını yeniden oku ancak yalnızca şu sütunları al:
    - order_id
    - customer_id
    - order_status
    - order_purchase_timestamp
5-  Yalnızca ilk 100 siparişi DataFrame'e aktar.
"""

klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"
dosya = r'\olist_orders_dataset.csv'

df = pd.read_csv(
    klasor + dosya
)

print(df.head(10))
print(df.shape)         ## Sütun ve satır sayısını verir
print(df.columns)       ## Sütun isimlerini verir.
print(df.dtypes)        ## Veri tiplerini verir.

df = pd.read_csv(
    klasor + dosya,
    usecols=['order_id','customer_id','order_status','order_purchase_timestamp']
)

print(df)

df = pd.read_csv(
    klasor + dosya,
    nrows=100
)

print(df)

klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"
dosya = r'\olist_order_items_dataset.csv'

df = pd.read_csv(
    klasor + dosya,
    usecols=['product_id','price'],
    nrows=10
)

print(df)       ## İlk 10 satırı dosyadaki ile aynı sıralama verdi

rapor = df.groupby('product_id',as_index=False).agg({
    'price':'sum'
})

rapor.columns = ['Ürün ID', 'Toplam Fiyat']
print(rapor)    ## İlk 10 satırı dosyadaki ile farklı sıralama verdi
