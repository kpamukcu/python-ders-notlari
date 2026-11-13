import pandas as pd         ## Pandas kütüphanesini yükler
import sqlite3              ## sqlite kütüphanesini yükler
import os                   ## Dosya işlemlerim kütüphanesini yükler

""" 
######## SQL ile DataFrame oluşturma #########

SQL (Structured Query Language), ilişkisel veritabanlarını yönetmek ve sorgulamak için kullanılan dildir.

Tablo	        İçerik
customers	    Müşteri bilgileri
orders	        Sipariş bilgileri
products	    Ürün bilgileri
payments	    Ödeme bilgileri
sellers	        Satıcı bilgileri

Bu tablolar arasında ilişkiler kurulabilir.

-   read_sql()  -> Sql veritabanlarından veri okuyabilmek için kullanılan pandas metodu.


Genel Syntax;

df = pd.read_sql(
    sql_sorgusu,
    connection
)

sql_sorgusu: Veritabanından hangi verilerin alınacağını belirtir.
connection: Veritabanı bağlantısını temsil eder.

Örnek vt için SQLite kullanılacak indirme linki: https://sqlitebrowser.org/dl/
Kurulan programın adı: DB Browser fo SQLite
"""


##### VERİ TABANI BAĞLANTISI OLUŞTURMA ######

klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

veritabani_yolu = os.path.join(
    klasor,
    'olist_dataset.db'
)

baglanti = sqlite3.connect(veritabani_yolu)

### DB'deki tabloları listeleme
tablolar = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table'",
    baglanti
)

print(tablolar)


### Python ile SQL'den veri çekme
sorgu = 'select * from orders limit 20'

df = pd.read_sql(sorgu,baglanti)
print(df)


### SQL'den bellirli sütunları çekmek ###
sorgu2 = """ select order_id, customer_id, order_status from orders """

df = pd.read_sql(
    sorgu2,
    baglanti
)

print(df)


### SQL'den belirli değeri olan kayıtları çekme ###

sorgu3 = """ 
    select * from orders
    where order_status = 'delivered'
    limit 50
 """

df = pd.read_sql(
    sorgu3,
    baglanti
)

print(df)

print(df.shape)
print(df.columns)
print(df.dtypes)


sorgu4 = """ select order_status from orders  """

df = pd.read_sql(
    sorgu4,
    baglanti
)

statu = df.groupby('order_status').size()
print(statu)


sorgu5 = """ select order_status, count(*) as toplam_siparis from orders group by order_status """

df = pd.read_sql(sorgu5,baglanti)
print(df)