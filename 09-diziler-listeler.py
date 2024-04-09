""" 
Diziler ve Listeler

1- Diziler (Array) -> Ard arda sıralanmış aynı tür elemanların oluşturduğu sıralı objelerdir.
    Sayı Dizisi:    1 7 9 15 78
    Char Dizisi:    T S F W  M
    indiz:          0 1 2 3  4

2- Diziler python'da listeler halinde ifade edilir. Listeler bir sıralı elaman dizisidir. Listeler tüm veri türlerini içinde barındırabilir.
    liste = ['Para1','Para2',5,'Para4']

3- Liste elemanlarına ulaşma: Liste içindeki bir parametreye ulaşmak için indis nosu ile ulaşabiliriz. İndisNo'lar sıfırdan başlar.
4- index(indisNO) ile bir liste içindeki bir parametrenin indisNosunu buluruz.
5- Liste Dilimleme için stringlerde de kullanılan [:] yöntemi kullanılabilir.
6- listeAdi.append() ile listenin sonuna yeni bir parametre ekleyebiliriz.
7- listeAdi.insert(indisNo,argüman) ile istediğimiz bir indisNo'ya yeni bir parametre ekleyebiliriz. Not: ekleme işlemi yapılmadan önceki indisNosu seçilen parametre silinmez.

"""

isim_liste = ['Ali','Veli','Hakan']
char_liste = ['*','-','?','/','u']
sayi_liste = [1,2,3,4,5]
bos_liste = []
kar_liste = [12,'*','kelime',"ra"]

liste = ['Hakan','Yılmaz',320,'Mehmet']
print(liste[2]) #Ekrana 320 yazacaktır.



### Bir Liste İçinde Bir Elemanın Indis Nosunu Bulma ###

Liste = [1,2,3,'a','2','Ali',2]
print(Liste.index(2)) #Ekrana 1 yazar
#print(Liste.index(5)) #Ekrana "5 is not in list" yazar


""" 
Stok Kontrol Programı (Not: İlgili ürün yoksa hata veriyor)

urunler = ['Kitap','Kalem','Silgi','Defter','Çanta']
bul = input('Lütfen Kategori girin.: ')

if(urunler.index(bul)>=0):
    print('Aradığını Ürün Stoklarımızda Mevcuttur.')
else:
    print('Aradığınız Ürün Stoklarımızda Yoktur.') 
"""

L = [1,2,3,4,5,6,7,8,9]
print(L[2:])    #Ekrana indisNo'su 2 olan parametreden itibaren ilgili değerleri yazar.
print(L[:3])    #Ekrana ilk 3 parametreyi yazdıracaktır.
print(L[::-1])  #Ekrana diziyi tersten yazacaktır.

L.append(10)    # L listesine(dizisine) 10 argümanını parametre olarak ekeleyecektir.
print(L)        # Ekrana [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] yazacaktır.
print(len(L))   # Ekrana 10 yazacaktır.

L.insert(2,'Hayko Cepkin')
print(L)


K = []
secim = input('Yeni Ürün Girmek İstiyor musunuz? (y/h).: ')

if(secim == 'y'):
    yeniPara = input('Lütfen Yeni Ürün İsmini Girin.: ')
    K.append(yeniPara)
    sor = input('Ürünler Listelensin mi? (y/h).: ')
    if(sor == 'y'):
        print(K)
    else:
        print('Yeni ürün eklendi')
else:
    print('Ürün Ekleme işlemi kullanıcı tarafından reddedildi')

##### ÖDEV -> Kullanıcı yeni kayıt işlemini bitirene kadar ürün girme işlemine devam etsin. (While döngüsü ile)