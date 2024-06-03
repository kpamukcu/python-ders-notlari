""" 
Modüller

Hazır kütüphaneler ve/veya bizim oluşturduğumuz kütüphaneler olup python algoritmalarını barındırmaktadır.
Hazır modüller için pypi.org sitesi kullanılabilir. Ayrıca python.org üzerinden indirilen python alt yapısı içinde hazır gelen modüller de mevcuttur.

"""

#YÖNTEM 1

#import math ### Math modülü projemize import edildi
#import math as islemler     ### şeklinde yapılan import sürecinde math modülünü islemler adıyla kulanıyor oluruz.

#value = dir(math) ### Math modülü içindeki fonksiyonları value değişkenine aktarıldı
#print(value) ### Math modülü içindeki fonksiyonların isimleri yazdırıldı

#value = help(math) ### Math modülündeki fonksiyonların açıklamalarını help fonksiyonu ile çekip value değişkenine akatarıldı.
#print(value) ### Math modülü içindeki fonksiyonların kullanım özellikler ve açıklamaları yazdırıldı

# value = math.sqrt(49)   #Karekök alma
# print(value)            #Ekrana 7 yazar.

# value = math.factorial(5) #5'in faktöriyel'ini hesaplar.
# print(value)            #Ekrana 120 yazar.

# value = math.floor(5.9) #İlgili float değeri aşağı yuvarlama yapar
# print(value)            #Ekrana 5 yazar

# value = math.ceil(5.9)  #İlgili float değeri yukarı yuvarlar
# print(value)            #Ekrana 6 yazar


# YÖNTEM 2
#from math import *  #Math modülünden tüm fonksiyonları import etmiş olduk. Bu durumda direkt olarak fonksiyonun adını yazarak çalıştırabiliriz.
from math import factorial,sqrt     #Bu yöntemde ise math modülü içinden sadece factorial ve sqrt fonksiyonlarını import etmiş oluyoruz. Performans açısından iyi bir yöntem.

value = factorial(5) #math ifadesini eklemeye gerek kalmadı
print(value) #Ekrana 120 yazar

value = sqrt(49)
print(value) #Ekrana 7 yazar
