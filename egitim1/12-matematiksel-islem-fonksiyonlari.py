""" 

1- round() ->  Fload bir değeri tam sayıya çevirir. Yukarı ya da aşağı yönlü yuvarlama yapacaktır.
2- max() & min() -> Girilen parametler arasındaki en büyük ve en küçük değerleri yakalar.
3- pow(x,y) -> x değerinin y değerinde kuvvetini hesaplar.
4- sum() -> girilen parametlerin toplamını hesaplar.
5- sqrt() -> değerin karakeökünü hesaplar. Ancak math modülü import edildiği taktirde kullanılanılabilir.
6- gcd() -> parametrelerin ortak bölenlerinin en büyüğünü bulur. Yani obeb'ini bulur. Ancak math modülü import edildiği taktirde kullanılanılabilir.
7- random() -> Rastegele fload türünde bir sayı üretecektir. Ancak random modülünün kurulması gerekemektedir.
8- randint() -> Rastgele belirlenen bir aralıkta integer bir sayı üretmek için kullanılır. Ancak random modülünün kurulması gerekemektedir.
9- randrange(a,b,c) -> üç ayrı parametre alır ve a ile b arasında c değeri kadar atlaya atlaya değer oluşturur. Ancak random modülünün kurulması gerekemektedir.
10- uniform() -> Griliken iki parametre arasında fload data türünde rastgele sayı üretecektir. Ancak random modülünün kurulması gerekemektedir.
11- choice() -> Liste içinden rastgele bir değer verir. Ancak random modülünün kurulması gerekemektedir.
12- shuffle() -> Liste içindeki elementleri rastgele sıralamak için kullanırlır.Ancak random modülünün kurulması gerekemektedir.
13- sample(liste, adet) -> Liste içinden rastgele istediğimiz kadar parametre seçmeyi sağlar. Ancak random modülünün kurulması gerekemektedir.

"""

print(round(2.13)) #Ekrana 2 Yazar
print(round(2.53)) #Ekrana 3 Yazar

print(max(5,8,98,-13)) #Ekrana 98 Yazar
print(min(5,8,98,-13)) #Ekrana -13 yazar

print(pow(2,3)) #2'nin 3. kuvvetini hesaplar. Ekrana 8 yazar.

print(sum([1,2,3,4,5,6,7,8]))
print(sum({1,2,3,4,5,6,7,8}))

import math
print(math.sqrt(144)) #Ekrana 12.0 yazar

print(math.gcd(524,9874))
print(math.gcd(81,27))

### Bir kürenin iç hacmini ve yüzey alanını hesaplama programı ###
### Kürenin Hacmi -> V = (4/3)*pi*yarıçapın kübü
### Kürenin Yüzey Alanı -> A = 4*pi*yarıçapın karesi

r = int(input('Yarı Çap Değerini Girin.: '))
Hacim = (4/3)*math.pi*pow(r,3)
Alan = 4*math.pi*pow(r,2)
print(f'Kürenin Hacmi: {Hacim} m^3, \nKürenin Alanı: {Alan} m^2.')

import random

print(random.random()) #Rasgete bir sayı üretecektir.
print(random.randint(1,9))
print(random.randrange(1,13,2)) #1 ile 13 arasında 2'şer atlayarak değer oluşturur.
print(random.uniform(1,16)) # 1 ile 16 arasında rastele bir fload değer verecektir.

Liste = ['Hayko','Mahmut','Ajdar','Bülent']
print(random.choice(Liste))

random.shuffle(Liste) #Liste içindeki isimlerin sırasını rastgele değiştirdi.
print(Liste) #Listenin yeni sıralı halini görebilmek için Liste dizisini ayrıca yazdırmak gerekmektedir.

print(random.sample(Liste,2)) #Liste içinde rastgele 2 parametre seçip ekrana yazar.


### Tahmin Oyunu ###
sayi = random.randint(1,6)
tahmin = int(input('Tahmininizi Girin.: '))
skor = 5
while True:
    if(sayi == tahmin):
        print(f'Tahmin Doğru. Skorunuz: {skor}')
        break
    else:
        skor -= 1
        if(tahmin < sayi):
            print(f'Yukarı!! Tekrar Deneyin. Skorunuz: {skor}')
            tahmin = int(input('Tahmininizi Girin.: '))
        else:
            print(f'Aşağı!! Tekrar Deneyin. Skorunuz: {skor}')
            tahmin = int(input('Tahmininizi Girin.: '))

### TAŞ - KAĞIT- MAKAS Oyunu ###
O = ['T','M','K']
R = random.choice(O)
S = input('Seçiminiz.: ').capitalize()

print(f'Bilgisayar {R} Seçti')
print(f'Sen {S} Seçtin')

if R == S:
    print('Berabere')
elif R == 'T' and S == 'M':
    print('Kaybettiniz')
elif R == 'T' and S == 'K':
    print('Kazandınız')
elif R == 'M' and S == 'T':
    print('Kazandınız')
elif R == 'M' and S == 'K':
    print('Kaybettiniz')
elif R == 'K' and S == 'T':
    print('Kaybettiniz')
elif R == 'K' and S == 'M':
    print('Kazandınız')
else:
    print('Geçersiz Giriş')


# while True:
#     if R == S:
#         print('Tekrar')
#         S = input('Seçiminiz.: ')
#     elif R == 'T' and S == 'M':
#         print(f'Kaybettiniz. Rakibiniz {R} seçti')
#         break
#     elif R == 'T' and S == 'K':
#         print(f'Kazandınız. Rakibiniz {R} seçti')
#         break
#     elif R == 'M' and S == 'T':
#         print(f'Kazandınız. Rakibiniz {R} seçti')
#         break
#     elif R == 'M' and S == 'K':
#         print(f'Kaybettiniz. Rakibiniz {R} seçti')
#         break
#     elif R == 'K' and S == 'T':
#         print(f'Kaybettiniz. Rakibiniz {R} seçti')
#         break
#     elif R == 'K' and S == 'M':
#         print(f'Kazandınız. Rakibiniz {R} seçti')
#         break
#     else:
#         print('Geçersiz Giriş')
#         S = input('Seçiminiz.: ')
