""" 
Date Time Modülü - 08:07

Tarih ve zamanla ilgili işlemler yapılacaksa date time modülü kullanılmaktadır.
Modülü kullanabilmek için datetime modülü import edilmelidir.

from datetime inport datetime -> datetime modülü içindeki hem zaman hem de tarih işlemleri için gerekli olan class import edilir
from datetime inport date -> datetime modülü içindeki sadece tarih işlemleri için gerekli olan class import edilir
from datetime inport time -> datetime modülü içindeki sadece zaman işlemleri için gerekli olan class import edilir
import datetime tüm modülü import eder.

1- datetime.now()   -> Şuanki tarih ve zaman bilgisini verir. alternatif kullanım olarak datetime.today() metodu da kullanılabilirdi
2- .year            -> Yıl bilgisini YYYY formatında verir.
3- .month           -> Ay bilgisini MM formatında verir. (1 ile 12 arasında değer verecektir.)
4- .day             -> Gün bilgisini verir. 1 ile 31 arasında değer verir. Ayın kaçıncı günü olduğu bilgisi
5- .hour            -> Saat bilgisini verir. 0 ile 23 arasında değer verir.
6- .minute          -> Dakika bilgisini verir. 0 ile 59 arasında değer verir.
7- .seconde         -> Saniye bilgisini verir. 0 ile 59 arasında değer verir.

Formatlanmış halde kullanım
8- datetime.ctime(parametre)                -> datetime.now() metotundan gelen değeri parametre olarak kullanır.
9- datetime.strftime(degiskenAdi, '%Y')     -> Yıl bilgisini string olarak türünde verecektir.
10- datetime.strftime(degiskenAdi, '%X')    -> HH:MM:SS bilgisini verir.
11- datetime.strftime(degiskenadi, '%d')    -> Gün bilgisini verir. (1 ile 31 arasında bir değer) Ayın kaçıncı günü olduğu bilgisi
12- datetime.strftime(degiskenadi, '%A')    -> Monday şeklinde gün bilgini verir. Haftanın hangi günü olduğunu verir.
13- datetime.strftime(degiskenAdi, '%B')    -> June şeklinde ay bilgisini verir.

Not: Formatlı kullanım için ikinci parametrelere https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes adresinden ulaşılabilir.

"""

from datetime import datetime

tarihZaman = datetime.now() 
print(tarihZaman)           # Şuana ait tarih ve zaman bilgisini verecektir.
print(tarihZaman.year)      # Yıl bilgisini YYYY formatında getirir.
print(tarihZaman.month)     # AY bilgisini verir.
print(tarihZaman.day)       # Gün bilgisini verir.
print(tarihZaman.hour)      # Saat bilgisni verir.
print(tarihZaman.minute)    # Dakika bilgisini verir.

print(datetime.ctime(tarihZaman))           # Sat Jun 22 02:22:24 2024 şeklinde daha anlamlı değer verir.
print(datetime.strftime(tarihZaman,'%Y'))   # Yıl bilgissini verir.
print(datetime.strftime(tarihZaman,'%X'))   # HH:MM:SS bilgisini verir.
print(datetime.strftime(tarihZaman,'%d'))   # Gün bilgisini verir. (1 ile 31 arasında bir değer) Ayın kaçıncı günü olduğu bilgisi
print(datetime.strftime(tarihZaman,'%A'))   # Monday şeklinde gün bilgini verir. Haftanın hangi günü olduğunu verir.
print(datetime.strftime(tarihZaman,'%B'))   # June şeklinde ay bilgisini verir.

print(datetime.strftime(tarihZaman, '%d %B %Y'))    # 14 June 2024 şeklinde bilgi verir.


t = '14 Kasım 2022'
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

