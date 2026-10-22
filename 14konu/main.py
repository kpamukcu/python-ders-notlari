""" 
PANDAS

- Pandas, bu tip tablo verilerini Python içinde kolayca yönetmeyi ve analiz etmeyi sağlayan bir kütüphanedir. CSV, Excel ve SQL gibi kaynaklardan veri okuyabilir; veriyi inceleyebilir, temizleyebilir, hesaplayabilir ve sonuçları dışarı aktarabilir.

Çalışma Şekli
Ham Veri (CSV, Excel, SQL) -> Pandas DataFrame (Veriyi düzenle, incele, temizle) -> Analiz ve Rapor (Hesaplamalar · Filtreler · İş kararları)

Örneğin satış dosyasındaki her sipariş için adet × birim fiyat hesabını yapabilir, ardından kategori bazında gelirleri kaşılaştırabilir. Böylece yalnızca veriyi göstermekle kalmaz, veriden anlamlı sonuçlar da çıkarılabilir.

- Pandas kütüphansesi projeye import edilmelidir.
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
Diyelim ki şirkete ait 50.000 sipariş içeren bir dosya mevcut ve şu soruların yanıtlarını isteniyor:

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


############## Pandas Serileri (Series) devam et ##############