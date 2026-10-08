""" 
Nesne Tabanlı Programlama OOP


"""

# Class oluşturuldu. Hiçbir özelliği yok şuan
class Runner:
    pass            #pass ile girilmesi gereken özellikleri geçici olarak durdurabiliriz.


runner1 = Runner()  #runner1, Runner class'ından oluşan bir nesne
runner2 = Runner()  #runner2, Runner class'ından oluşan bir nesne

#özellik ekleme
runner1.name = 'Kaan'
runner1.age = 44
runner1.weight = 67

runner2.name = 'Batuhan'
runner2.age = 39
runner2.weight = 65

print(runner1.name)     #Ekrana Kaan yazar
print(runner2.name)     #Ekrana Batuhan yazar

#__init__ (Metot yapıcı)
class Runner:
    def __init__(self,name,age,weight):         #self, üzerinde işlem yapılan nesnenin kendisini ifade eder. Yani runner1, runner2, runner3 ifade eder
        self.name = name                        #self.name = runner1.name ile aynıdır.
        self.age = age                          #self.age = runner1.age ile aynıdır.
        self.weight = weight                    #self.weight = runner1.weight ile aynıdır.

runner3 = Runner('Hakan',35,70)

print(runner3.name)


#Metot oluşturma (Davranış Ekleme)
class Runner:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi

## Örnek -> Bir koşucunun VKE'sini hesaplama
isim = input('Koşucu Adını Girin: ')
yas = int(input('Koşucunun Yaşını Girin: '))
agirlik = int(input('Koşucunun Kilosunu Girin: '))
boy = float(input('Koşucunun Boy Bilgisini Girin: '))

kosucu = Runner(isim,yas,agirlik,boy)
print(f"{kosucu.age} yaşındaki {kosucu.name}, {kosucu.weight} kiloda olup vücut kitle endeksi {kosucu.calculate_bmi()}")


##Örnek -> VKE ve Performans Hesaplayıcı
class Runner:
    def __init__(self,isim,yas,kilo,boy,sure10k):
        self.isim = isim
        self.yas = yas
        self.kilo = kilo
        self.boy = boy
        self.sure10k = sure10k

    def calculate_bmi(self):
        bmi = self.kilo / (self.boy **2)
        return bmi

    def calculate_10k_pace(self):
        pace = self.sure10k / 10
        return pace

    def show_info(self):
        print(f'Koşucu: {self.isim}')
        print(f'Yaş: {self.yas}')
        print(f'Kilo: {self.kilo}')
        print(f'Boy: {self.boy}')
        print(f'Toplam Süre: {self.sure10k}')
        print(f'Pace: {self.calculate_10k_pace()}')
        print(f'VKE: {self.calculate_bmi()}')

name = input('Koşucunun Adını Girin: ')
age = int(input('Koşucunun Yaşını Girin: '))
weight = int(input('Koşucunun Kilosunu Girin: '))
height= float(input('Koşucunun Boyunu Girin:'))
sumTime = int(input('Koşucunun Toplam Koşu Süresini dk cinsinden girin: '))

kosucu = Runner(name,age,weight,height,sumTime)

kosucu.show_info()


kosucu_1 = Runner('Kaan',44,66,1.68,51.28)
kosucu_2 = Runner('Ahmet',32,72,1.80,48.5)

kosucu_1.show_info()
kosucu_2.show_info()

#amount -> Metoda attribute'larda olmayan bir yeni değeri dışarıdan göndermektir.
#Örnek -> Banka Hesabı
print('Banka Hesabı OOP Uygulaması')


class BankAccount:
    def __init__(self,owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} hesabının bakiyesi: {self.balance}₺'dir.")

    def deposit(self,paraYatir):
        self.balance = self.balance + paraYatir
        print(f'{self.owner} hesabına {paraYatir}₺ eklenmiş olup güncel bakiye: {self.balance}')

    def withdraw(self,paraCek):          

        if paraCek > self.balance:
            print(f'Yetersiz Bakiye. Güncel Bakiyeniz: {self.balance}')
        else:
            self.balance = self.balance-paraCek
            print(f'Hesabınızdan {paraCek}₺ çekilmiş olup güncel bakiyeniz: {self.balance}')


account1 = BankAccount("Kaan", "TR001", 10000)
account2 = BankAccount("Ahmet", "TR002", 5000)

account1.show_balance()
account2.show_balance()
account1.deposit(5000)
account1.withdraw(3000)
account2.withdraw(20000)
