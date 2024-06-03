'''
VERİ TÜRLERİ (DATA TYPES)

int -> Tamsayı veri tipidir. Integer veri türü olarak geçer.
float -> Ondalıklı sayı veri tipidir.
bool -> Doğru / Yanlış (true / false) veri tipidir. Mantıksal Veri türü (Boolean) olarak da geçer.
str -> Karakter veri tipidir. String veri türü diye geçer.

bir verinin data türünü alabilmek için type() metodu kullanılır.

Not:
a) =   -> Atama Operatörüdür.
b) ==  -> Eşitlik Operatörüdür.
c) === -> Denklik Operatörüdür.
d) Dataların veri türlerini değiştirmek istersek ilgili datanın başına değiştirilmesini istediğimiz data türünü yazmamız yeterli
    ör: 4.5 float değeri float(4.5) ile 4'e dönüştürüp data türünü int olarak değiştirmiş olacaktır.

'''

a = 3
b= 4.5
isim = 'Hakan'
print(type(a))      #Ekrana int yazar
print(type(b))      #Ekrana float yazar
print(type(isim))   #Ekrana str yazar
print(b>a)          #Ekrana true yazar
print(a>b)          #Ekrana false yazar
print(type(b>a))    #Ekrana bool yazar.

print(int(4.5))     #Ekrana 4.5 değerini 4 olarak yazar ve data türünü int olarak değiştirmiş olur.
print(str(4))       #Ekrana 4 int değerini yine 4 olarak yazar ancak type() ile kontrol edildiğinde str olarak görünecektir.

#Not: Metinsel str bir değeri int değere dönüştüremeyiz.