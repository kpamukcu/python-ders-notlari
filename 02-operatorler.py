'''
OPERATÖRLER

- Python'da kullanılan matematiksel operatörler (+,-,/,*,//,%)
- Matematiksel işlem öncelikleri Python'da da geçerlidir. İşlem önceliği sıralaması ise şu şekildedir.
  Pazrantez içi -> Üs Alma -> Çarpma -> Bölme -> Mod Alma -> Toplama -> Çıkarma


'''

#Toplama Operatörü (+)
print(3+5) #Ekrana 8 yazar

#Çıkarma Operatörü (-)
print(10-2) #Ekrana 8 yazar

#Çarpma Operatörü (*)
print(4*2) #Ekrana 8 yazar

#Bölme Operatörü (/)
print(16/2) #Ekrana 8.0 yazar. Çünkü bölme işleminin sonucu ondalıklı olabilir. Onadlıklı sayılar Data Türü olarak Float geçmektedir.

#Tam Sayı Bölme Operatörü (//)
print(26//5) #Ekrana, 26'nın 5'e bölümü ile 5.2 sonucunun sadece tam sayı kısmını yani 5'i yazar. 

#Kalan Operatörü (Mod Alma %)
print(41%3) #Ekrana 2 Yazar

#Üs Alma (**)
print(2**3) #Ekrana 8 yazar

#İşlem Önceliği Ör:
print(3+5*2) #ekrana 13 yazar. İşlem öncelik sıralamasına önce çarpama sonra toplama işlemi yapılacaktır.
print(2+3*2**2) #ekrana 14 yazar. işlem öncelik sıralamasına göre önce üs alma sonra çarpma sonra toplama işlemi yapılacaktır.
print((5-3)*5+2) #ekrana 12 yazar. işlem öncelik sırasına göre önce parantez ii sonra çarpma sonra da toplama işlemi yapılacaktır.

#Soru: operatorler-img-1 isimli görseldeki formülü python dilinde yazıp sonucu ekrana yazdır.

x= (2**2+3/5) / (3**2-2*5)
print(x)