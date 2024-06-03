'''
Fonksiyonlar

1) Fonksiyon -> Programın belli işlevini(görevini) yerine getiren küçük program parçalarıdır.
Fonksiyonların totali ile ana program oluştur. Legodan ev yapmak gibi düşünebiliriz. Her bir lego parçası fonksiyon olup legoların birleşimi ile ev oluşturmuş oluruz gibi.

Not: Fonksiyon yapısı için fonksiyon-yapisi.png ve fonksiyon-yapisi.png görseli incelenebilir.

2) Bir fonksiyon birden fazla kez çağrılabilir.
3) Özel bir fonksiyo oluşturmak için def anahtar kelimesi ile tanımlanır. Not: def, defination function kelimsinin kısaltmasıdır.

def fonksiyonAdı():
    bu fonksiyon çağırıldığında çalışacak kodlar

fonksiyonAdı() -> fonksiyon çağırmak için sadece adını ve parametre parantezini yazmak yeterli olur.

4) Parantezler için parametreler girilebilir. Parametre, bir fonksiyon çalışırken kullanılmasını istediğimiz değerlerdir. Argüman olarak da isimlendirilirler.

5) return() -> Bir fonksiyonun yaptığı işlemler doğrultusunda ulaştığı değere bizim de ana program içinde ulaşıp kullanabilmemiz için return() komutu kullanılır.

6) Local Değişken:
        Fonksiyon kod kümesi içinde tanımlanan ya da oluşan değişkenler local değişkenlerdir ve o değişken sadece o fonksiyon içinde kullanılabilir.

7) Global Değişken:
        Bir değişkenin her yerden erişilebilir olması için fonksiyon dışında oluşturulmalı veya global kampsamda bildirilmesi gerekmektedir. Bu değişkenlere ise gloabl değilen denir.

8) def ile fonksiyon oluşturulmuş ama içeriği olmayan bir yapı oluşturmak istiyorsan. Yani programı ana hatlarıyla oluşturup daha sonra alt fonksiyonları oluşturmak istiyorsan oluşturduğumuz alt fonksiyonlara pass veya sadece return yazarak none değerli bir fonksiyon oluşturabiliriz.

9) Fonksiyon Kısaltma (lambda) -> tek satırlık bir fonksiyon yazılacaksa kullanılabilir.

def dolar(TL):            yerine        dolar = lambda TL: TL/18    tek satırlık olduğu için bu kullanılabilir.
    return(TL/18)


10) Öz Yinelemeli (Rekürsif) fonksiyon -> Bir fonksiyonun içeriside yine ayı fonksiyonu çağırırsak bu öz tekrarlı fonksiyondur.

'''

def topla():    #fonksiyon tanımlandı
    print(5+2)  #fonksiyon çağırıldığında çalışacak olan kod kümesi

topla()         #fonksiyon çağrıldı. Eğer çağırılmazsa tanımlanan işlem grubu çalışmaycak ve ilgili response(sonuç) ekrana gelmeyecektir.


#Restoran misafir karşılama örneği
def selamlama(isim):
    print(f'Sayın {isim} restoranımıza hoşgeldiniz.')

Ad = input('İsminiz Nedir? ')
selamlama(Ad)

#Bu örneğe göre misafirden alınan isim bilgisi Ad değişkenine atandı ve bu değişken selamlama() fonksiyonun parametre parantesine yazılarak çağırıldı ve böylelikle def selamlama(isim) fonksiyonu çalıştırıldı. çağırılırken kullanılan ad değişkeni def selamlama(isim): fonksiyonundaki isim parametresinin argümanıdır.Yani ad değişkenine atanan değer isim parametresine gitmiş olacaktır. while true: döngüsü ile isim alma ve işlemini sürekli çalıştırabiliriz.

""" 
def merhaba(name):
    print(f'Sevgili misafirimiz {name}, restoranımıza hoşgeldiniz')

while True:
    adi = input('\nAdınızı Girin? ')
    if(adi != '0'):
        merhaba(adi)
    else:
        print('Çıkış Yaptınız')
        break 
"""

# Kullanıcı Adı ve şifre sorgulama ekranı. Eğer hatalı girerse tekrar giriş yapması isteniyor.
def login():
    kadi = input('\nKullanıcı Adınızı Girin? ')
    sifre = input('Şifrenizi Girin? ')

    while (kadi == 'Admin' and sifre == '123'):
        print(f'Sevgili {kadi}, yönetim paneline hoşgeldin')
        break
    else:
        print('\nKullanıcı Adınız ve/veya şifreniz hatalı. Lütfen Tekrar deneyin')
        login()

login()



#### Bir Dikdörtgenin alanını hesaplama (Return(9) kodu ile) ####

def alan(u,g):
    A = u*g
    return A        #Yapılan işlem sonucuna bir değer oluştu ve bu değere fonksion dışında ulaşabilmek için return kodu kullanıldı

def cevre(u,g):
    C = 2*(u+g)
    return C        #Yapılan işlem sonucuna bir değer oluştu ve bu değere fonksion dışında ulaşabilmek için return kodu kullanıldı

u= int(input('Uzun Kenar Ölçüsünü Girin.: '))
g= int(input('Kısa Kenar Ölçüsünü Girin.: '))

print(f'Alanı: {alan(u,g)}m^2, Çevresi: {cevre(u,g)}m')


def topla():
    global b #***** Bu bildirim 107. satırdaki önek yapılırken eklenecek
    a = 5
    b = 6
    return (a+b)

print(topla()) #Ekrana 11 yazar
#print(a) #Loacal bir değiken olduğu için a değişkeni tanımlanmadı hatası verecektir. Eğer a değişkeni topla() fonksiyonun dışında tanımanırsa ya da fonksiyon içinde global a bildirimi yapılsaydı 5 değerini ekrana yazdıracaktır.
print(b) #Ekrana 6 yazacaktır. Çünkü b değişkeni fonksiyon içinde global olarak bildirildi.


#Öz Yinelemeli fonksiyon örneği
def ustAl(s1,s2):
    if s2==0:
        return 1
    else:
        return(s1*ustAl(s1,s2-1))
    
print(ustAl(2,4))