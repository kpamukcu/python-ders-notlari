""" 
Nesne ve Sınıf

1- class anahtar kelimesi ile tanımlanırlar.

    class Araba(marka):
        model = marka
        def metot(self):
            self.marka = 'Mercedes'

Not: Class'lar altında tanımlanan fonksiyonlara metot denir.
            
2- self -> class içindeki erişilebilecek elemanlar için kullanılır. Nesnenin kendisini referans etmesini sağlar. Yani sözü edilen nesneyi doğrudan işaret eder. 

3- Nesne Tanımlama

    class hayvan():
        pass

    class araba():
        pass

    at =  hayvan()
    horoz = hayvan()

    taksi = araba()
    kamyon = araba()

4- Oluşturulan sınıfların sahip olduğu özellikleri öğrenmek için dir(nesneAdı) ör: dir(Taksi)
5- Katılım (inheritance) -> Üst sınıfa ait olan özelliklerin alt sınıflara öiras olarak aktarılması özelliğidir. Böylece alt sınıf üst sınıfın özelliklerini taşır.

6- Modül Kavramı; her bir oluşturulan py uzantılı dosya bir modüldür. Kendimizin oluşturduğu modülleri veya ön tanımlı modülleri import ederek yeni bir python dosyasında çalışıtırabiliriz.
ör: import random   yazarak random.py dosyasının yeni kod sayfamıza import etmiş oluyoruz.

import edilen modülün programı direkt olarak ekleniyor ve programın çalışan haline ulaşabiliyoruz ancak modülün içindeki fonksiyonlara tek ek ulaşamayız.

Ancak from modulAdı import *    ile modülün içindeki tüm fonksiyonlara tek tek ulaşabiliriz.
Ayrıca from modulAdi import fonksiyonAdi ile o modülün içindeki sadece belirlenen fonksiyonu çağımış oluruz.


"""

import matematik
from matematik import *


class Araba():
    def __init__(self,model,marka,renk): # Bu fonksiyon class altında tanımlandığı için sınıf metodu olarak geçmeketedir.
        self.model = model
        self.marka = marka
        self.renk = renk

    def aracBilgisi(self): #Bu fonksiyon class'ın altında ve nesnelere yönelik olduğu için nesne metodu olarak geçemketedir.
        print(f'Markası: {self.marka}')
        print(f'Markası: {self.model}')
        print(f'Markası: {self.renk}')

Taksi=Araba(2020,'Fiat','Yeşil') #Araba sınıfı içinde oluşturulan Taksi nesnesidir. 2020 = model , Fiat = marka, Yeşil = renk özelliklerine denk gelmektedir.

print(Taksi.model) # Ekrana 2020 yazar
print(Taksi.marka) # Ekrana Fiat yazar
print(Taksi.renk) # Ekrana Yeşil yazar

kamyon = Araba(2012,'Man','Siyah')
print(kamyon.marka)

Taksi.aracBilgisi() #Ekrana Markası: Fiat - Markası: 2020 - Markası: Yeşil

motorsiklet = Araba(2024,'Pulsar','Gri') #motorskilet isimli nesne ouşturduk.
motorsiklet.aracBilgisi() #motorsiklet isimli nesneden aracBilgisi() nesne metodu ile verileri çektik



#Site üyelik sistemi
class uye():
    def __init__ (self,adi,soyadi,dogum):
        self.adi = adi
        self.soyadi = soyadi
        self.dogum = dogum
    def uyeInfo(self):
        print(f'Ad Soyad: {self.adi} \nSoyadi: {self.soyadi} \nDoğum Tarihi: {self.dogum}')

info = uye('Kaan','Pamukcu','1982')
info.uyeInfo()


## Kalıtım ##
class araba: #Üst Sınıf
    def __init__(self,model,fiyat):
        self.model = model
        self.fiyat = fiyat

class kamyon(araba): #alt sınıf
    def __init__(self,model,fiyat,renk):
        araba.__init__(self,model,fiyat)
        self.renk = renk

k1 = kamyon(2020,120000,'Kırmızı')
print(k1.model)
print(k1.fiyat)
print(k1.renk)

##############################################################
class Person:
    # class attributes (Her zaman kullanılmayacak olan attribute'ları class attribute olarak tanımla)
    adres = 'Lorem Ipsum Dolor Sit Amet Kadıköy / İstanbul'
    # Constractor (Yapıcı Metot)
    def __init__(self, name, year):
    # object attributes (Her zamana kullanılacak ve zorunlu olan attribute'ları object attribute olarak tanımla)
        self.name = name
        self.birthYear = year
    # instance methods
    def intro(self):
        print('Merhaba')

#Object(instance)
p1 = Person('Kaan',1980)


print(p1.name) ## Ekrana Kaan yazar
print(p1.birthYear) ## Ekrana 1980 yazar

##############################################################

para1 = input('Adınız Soyadınız.: ')
para2 = int(input('Doğum Yılınız.: '))
para3 = input('Telefon Numaranız.: ')

class Uyeler:
    adres = 'Lorem Ipsum Dolor Sit Amet Kadıköy - İstanbul'
    def __init__(self,name,year,phone):
        self.isim = name
        self.dogum = year
        self.tel = phone
    def intro(self):
        print('Merhaba ' + self.isim)
    def age(self):
        return 2024 - self.dogum


p1 = Uyeler(para1, para2, para3)

# Updating
# p1.isim = 'Mahmut'

#Accesing Object Attributes
print(f'{p1.isim} / {p1.dogum} / {p1.tel} / {p1.adres}')

p1.intro()
print(p1.age())




##############################################################

### Inheritance (Kalıtım): Miras Alma
# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastname = lname
        print('Person Created')

class Student(Person): #Person'ın sahip olduğu tüm özellikler Student class'ına da atanmış oldu
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname) # Ekrana 'Person Created' yazar
        print('Student Created') # Ekrana 'Student Created' yazar


p1 = Person('Hakan','Yılmaz') #Ekrana sadece 'Person Created' gelecektir.
s1 = Student('Mahmut','Tuncer') #Ekrana önce 'Person Created'sonra da 'Student Created' gelecektir.

print(f'Merhaba ben {p1.firstName} {p1.lastname}')
print(f'Merhaba ben {s1.firstName} {s1.lastname}')


