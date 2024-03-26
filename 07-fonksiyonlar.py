'''
Fonksiyonlar

Fonksiyon -> Programın belli işlevini(görevini) yerine getiren küçük program parçalarıdır.
Fonksiyonların totali ile ana program oluştur. Legodan ev yapmak gibi düşünebiliriz. Her bir lego parçası fonksiyon olup legoların birleşimi ile ev oluşturmuş oluruz gibi.

Not: Fonksiyon yapısı için fonksiyon-yapisi.png ve fonksiyon-yapisi.png görseli incelenebilir.

Bir fonksiyon birden fazla kez çağrılabilir.

Özel bir fonksiyo oluşturmak için def anahtar kelimesi ile tanımlanır. Not: def, defination function kelimsinin kısaltmasıdır.

def fonksiyonAdı():
    bu fonksiyon çağırıldığında çalışacak kodlar

fonksiyonAdı() -> fonksiyon çağırmak için sadece adını ve parametre parantezini yazmak yeterli olur.

Parantezler için parametreler girilebilir. Parametre, bir fonksiyon çalışırken kullanılmasını istediğimiz değerlerdir. Argüman olarak da isimlendirilirler.

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