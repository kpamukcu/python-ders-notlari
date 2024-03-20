'''
KOŞULLU İFADELER

- if -> Tek koşula bağlı gerçekleşecek işlemler için
- if else -> Çift koşula bağlı gerçekleşecek işlemler için
- if elif else -> Çoklu koşula bağlı gerçekleşecek işlemler için


KARŞILAŞTIRMA OPERATÖTLERİ
Koşul içerisindeki verilerin birbiriyle karşılaştırılmasında kullanılır. Bu operatörler sonuç doğruyasa true yanlışsa false sonuçlarını döndürürler.

==  ->  Eşittir
!=  ->  Eşit Değildir
>   ->  Büyüktür
<   ->  Küçüktür
>=  ->  Büyük eşittir
<=  ->  Küçük eşittir

Not: Koşul kontrol aşamasından birden fazla değer kontrol edilecekse and, or veya not mantıksal operatörleri kullanılır.
'''

print(8>3) #Ekrana true sonucunu yazar
print(8<3) #Ekrana false sonucunu yazar

a=5
b=3
print(a==b) #Ekrana false yazar.

print((3<5) and (4<7)) #Ekrana true sonucu dönecektir.
print((3<5) and (4<7) and (8<2)) #Ekrana false sonucu dönecektir.
print((3<5) or (4<7)) #Ekrana true sonucunu döndürecektir.
print((3<5) or (7<4)) #Ekrana true sonucu döndürür. Çünkü iki koşuldan biri doğru
print((3<5) or (7<4) or (7==9)) #Ekrana true sonucunu döndürür. Çünkü koşullardan biri doğru
print((3>=5) or (7<4) or (7==9)) #Ekrana false sonucunu döndürür. Çünkü koşullardan hiçbiri doğru değil
print(not(3>7)) #ekrana true sonucunu döndürecek. not ifadesi koşulun tersini kontrol edecektir.

if 5==5:
    print('5, 5\'e eşittir')


#Tahmin Oyunu
a = 25
b = int(input('Sayıyı Tahmin Et '))

if a == b:
    print('Tahmin Doğru')
else:
    print('Tekrar Deneyin')

#Not: Bu oyun şimdilik tek tahmin girme imkanı veriyor. Hatalı tahmin girildiğinde tekrar tahmin girebilme özelliği döngüleri ile yapılabilir.

#Sınav Notu Değerlendirme
Not = float(input('Not Giriniz: ')) #Burayı int'e çevirmek yerine float'a çevirmek gerekir. çünkü öğrenci notu ondalıklı bir der olabilir.

if(Not >= 50):
    print('Öğrenci Başarılı')
else:
    print('Öğrenci Başarısız')


#Kullanıcı Adı ve Şifre Kontrolü
    
user = input('Kullanıcı Adınızı Girin: ')
password = input('Şifrenizi Girin: ')

if user == 'Admin' and password == '123':
    print('Sevgili Admin Hoşgeldin')
elif user == 'Kadmin' and password == '456':
    print('Sevgili Kadmin Hoşgeldin')
else:
    print('Kullanıcı Adı ve/veya şifreniz hatalı.')