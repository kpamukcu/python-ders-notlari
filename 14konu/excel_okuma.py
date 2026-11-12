""" 
XLSX ile DataFrame oluşturma (Excel Dosyası Okuma)
Öncelikle Excel okuma işlemi için terminal üzerinden pip install openpyxl ile openpyxl motoru kurulmalıdır.

-   .read_excel()   -> Excel dosyalarını DataFrame'e dönüştürmek için read_excel() metodunu kullanır.

Parametre	            Görevi
sheet_name	            Okunacak çalışma sayfasını belirler.
usecols	                Yalnızca istenen sütunları okur.
nrows	                Okunacak satır sayısını sınırlar.
skiprows	            Belirtilen satırları atlar.
index_col	            Hangi sütunun index olacağını belirler.
header	                Sütun isimlerinin hangi satırda olduğunu belirler.
engine	                Excel okuma motorunu belirler.

-   to_excel()  -> Bu metot DataFrame'i Excel dosyasına aktarır.

"""

import pandas as pd
import os


klasor = r"C:\Users\kaan.pamukcu\Desktop\Kaan\python-ders-notlari\olist_dataset"

df = pd.read_csv(
    os.path.join(klasor,'olist_orders_dataset.csv')             #klasor + r'olist_orders_dataset.csv' yönteminden daha sağlıklı birleştirme
)

df.to_excel(
    os.path.join(klasor,'olist_orders_dataset.xlsx'),
    index=False                         #index=False kullanmamızın nedeni, Pandas'ın DataFrame index değerlerini Excel'e fazladan bir sütun olarak yazmasını önlemektir.
)


df = pd.read_excel(
    os.path.join(klasor,'olist_orders_dataset.xlsx')
)

print(df.head())


#### Excel sayfası okuma
# df = pd.read_excel(
#     os.path.join(klasor,'olist_orders_dataset.xlsx'),
#     sheet_name='Ocak'                           ## Sheet ismi "Ocak" olan sayfayı okur. Ancak elimizdeki dosya tek sayfa.
# )

#### Excel dosyasındaki sayfaların isimlerini yazdırma
# excel = pd.ExcelFile(
#     os.path.join(klasor,'olist_orders_dataset.xlsx')
# )

# print(excel.sheet_names)