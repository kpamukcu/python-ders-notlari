""" 
Diziler ve Listeler

1- Diziler (Array) -> Ard arda sıralanmış aynı tür elemanların oluşturduğu sıralı objelerdir.
    Sayı Dizisi:    1 7 9 15 78
    Char Dizisi:    T S F W  M
    indis:          0 1 2 3  4

2- Diziler python'da listeler halinde ifade edilir. Listeler bir sıralı elaman dizisidir. Listeler tüm veri türlerini içinde barındırabilir.
    liste = ['Para1','Para2',5,'Para4']

3- Liste elemanlarına ulaşma: Liste içindeki bir parametreye ulaşmak için indis nosu ile ulaşabiliriz. İndisNo'lar sıfırdan başlar.
4- index(indisNO) ile bir liste içindeki bir parametrenin indisNosunu buluruz.
5- Liste Dilimleme için stringlerde de kullanılan [:] yöntemi kullanılabilir.
6- listeAdi.append() ile listenin sonuna yeni bir parametre ekleyebiliriz.
7- listeAdi.insert(indisNo,argüman) ile istediğimiz bir indisNo'ya yeni bir parametre ekleyebiliriz. Not: ekleme işlemi yapılmadan önceki indisNosu seçilen parametre silinmez.
8- Bir liste içindeki parametrelerin sayısını bulabilmek için len() fonksiyonu'u kullanılabilir.
9- Bir liste içindeki bir değerin kaç adet olduğunu bulabilmek için .count(değer) metotu kullanılır. Ör: listeAdi.count('Python')
10- İki listeyi birleştirmek için toplama(+) operatörü kullanılabilir ancak listeAdi1.extend(listeAdi2) metotu ile birleştirme yapılmaktadır. extend ile yapılan birleştirme işleminde listeAdi2'nin değerleri listeAdi1'e atanmaktadır.Yani birleştirilmiş datayı görebilmek için lieteAdi1'i yazdırmak gerekmektedir.
11- Bir dizi içindeki parametreleri terse döndürmek için reverse() fonksiyonu kullanılır.
12- Bir liste içindeki int parametlere arasında en küçük ve en büyük değeri bulmak için min() ve max() fonkyionları kullanılır.
13- String bir ifadeyi listeye dönüştürmek için list('String ifade' veya string değişken Adı) fonksiyonu kullanılır.
14- Bir liste içinden istenilen değerleri silmek için remove() fonksiyonu kullanılır.
15- pop(indisNO) ile liste içindeki indisNosu belirlenen bir karakteri silme işlemini yapar. Eğer parantez içine indisNo yazılmazsa listedeki son parametreyi silecektir.
16- listeAdi.clear()  ile listenin içindeki tüm parametreleri siler.
17- Bir liste içinde bir argümanın olup olmadığını kontrol etmek için "in" ve/veya "not in" yöntemleri kullanılır.
18- Liste parametrelerini a'dan z'ye veya küçükten büyüğe sıralamak için listeAdi.sort() fonksiyonu kullanılır.
    Z'den a'ya veya büyükten küçüğe doğru sıralamak direkt olarak yoktur. Bunun için şu iki yönetmi kullanabiliriz
    
    1. Yöntem: liste artan yönde sıralandıktan sonra listeAdi = listeAdi[::-1] ile azalan yönde sıralama yaptırılabilir.
    2. Yöntem: liste artan yönde sıralandıktan sonra listeAdi.reverse() fonksiyonu ile azalan yönde sıralama yaptırılabilir.

19- Bir listenin elemanlarını umaralandırmak istenirse enumarate() fonksiyonu kullanılır.
20- Listenden yığın oluşturma: Eleman ekleme ve çıkarma işlemlerinin listenin en son elemanı üzerinden gerçekleştiği özel bir yapıdır. Listeye son giren ilk çıkar (Last In - First Out) Ör: üst üste dizilen kitaplar gibi düşünülebilir. En alttaki kitaba ulaşmak için üstündekileri sırayla kaldırmak gerekir.
21- Listeden kutruk oluşturma: eleman ekleme işleminin listenin sonundan ve çıkama işlemlerinin listenin başından gerçekleştiği özel bir yapıdır. Listeye son giren son çıkar (Last in - Last Out) Ör: Atm sırasındaki kullanıcılar

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

#### Kullanıcı yeni kayıt işlemini biterene kadar ürün girme uygulaması
urunler = []
print('İşlemi Tamamlamak için 0\'a Basın.')

while True:
    yeniUrun = input('Yeni Ürün Girin.: ')
    if yeniUrun != '0':
        urunler.append(yeniUrun)
    else:
        print(urunler)
        break


### Liste uzunluğunu bulmak
L = [1,3,6,5,8,9,1,2,'ta','-']
print(len(L)) #Ekrana 10 yazacaktır.

print(L.count(1)) #Ekrana 1 paratmeresinin L dizisinde kaç adet olduğunu yazacaktır.

# Listeleri Birleştirme
#Yöntem 1
S1 = [1,2,3,4]
S2 = [5,6,7,8]
S3 = S1 + S2
print(S3)

#Yöntem 2
S1.extend(S2) # S2 listesinin değerlerini S1 dizisine aktardı.
print(S1) ####[1, 2, 3, 4, 5, 6, 7, 8] ekrana yazacaktır.


# Liste paramtelerini tterse çevirme
uyeler = ['Hayko','Mahmut','Bülent']
uyeler.reverse() # Liste içindeki parametleri tersten sıralanacak şekilde uyeler listesine atama yaptı
print(uyeler) # Ekrana ['Bülent', 'Mahmut', 'Hayko'] yazar

#En küçük ve En büyük değerleri bulmak
sayilar = [12,332,5,4969,123548]
print(min(sayilar)) #Ekrana 5 yazar
print(max(sayilar)) #Ekrana 123548 yazar

#Kullanıcıdan alınan 5 adet rakamlardan en büyük ve en küçüğünün toplamını bulan ve girilen rakamların artimetik ortalamasını bulan uygulama yazın.
L = []
topla = 0
for i in range(5):
    sayi = int(input('Sayı Girin.: '))
    L.append(sayi)
    topla += sayi

print(f'Girilen Sayılardan En Büyük ve En Küçüğünün Toplamı: {max(L) + min(L)}')
print(f'Girilen sayıların artimetik ortalaması: {topla/len(L)}')


#String ifadeyi listeye çevirme
kelime = 'ARIBİLGİAKADEMİ'
L = list(kelime)
print(L) #Ekrana ['A', 'R', 'I', 'B', 'İ', 'L', 'G', 'İ', 'A', 'K', 'A', 'D', 'E', 'M', 'İ'] yazar
print(L.count('A')) #Ekrana 3 yazar

L.remove('İ') #Sadece ilk 'i' karakterini siler. Tüm İ karaterlerini silmek için döngüye girmelidir.
print(L)

#### String bir değerden belirlenen bir karaterlerin tümünü silmek ####
isim = 'KAANPAMUKCU'
L= list(isim) #isim string değişkenindeki değer karakter karakter L listesine atandı

for i in range(L.count('A')):  #L.count('A') ile döngünün kaç defa tekrarlanacağını oluşturulan liste içindeki karaktrer sayısına göre belirledi.
    L.remove('A') #L listesi içindeki A karakterlerini tek tek sildi

print(L) #Ekrana ['K', 'N', 'P', 'M', 'U', 'K', 'C', 'U'] yazar


#Listenin tamamını temizleme
L.clear()
print(L) #Ekrana [] yazar.

#Bir Liste içinde bir argümanın olup olmadığını kontrol etmek
uyeler = ['Hayko','Mahmut','Ajdar']
print('Hayko' in uyeler) #Ekrana True yazar
print('Hakan' in uyeler) #Ekrana False yazar

#Liste elemanlarını sıralama
Lsayi = [22,78,14,963,1,79543]
print(Lsayi) #Ekrana [22,78,14,963,1,79543] yazar

#Lsayi = Lsayi[::-1]
Lsayi.reverse()
print(Lsayi) #Ekrana [79543, 1, 963, 14, 78, 22] yazar


#Liste Elemanlarını Numaralandırma
gun = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']

for i, deger in enumerate(gun):
    print(str(i+1)+'.gün '+deger)

### VEYA ###

for i in range(len(gun)):
    print(f'{i+1}.gün {gun[i]}')


### Restoran Sıra Uygulaması

L = []

while True:
    isim = input('İsim Giriniz.: ')
    if isim != 'sıradaki' and isim != 'listele' and isim != 'bitti':
        L.append(isim)
    elif isim == 'sıradaki':
        if len(L) > 0:
            print(L.pop(0))
        else:
            print('Sırada kimse yok')
    elif isim == 'listele':
        if len(L) > 0:
            for i in range(len(L)):
                print(f'{i+1}. {L[i]}')
            sil = input('Listen çıkartmak istediğiniz mi var(e/h).: ')
            if sil == 'e':
                kim = int(input('Sİlmek istediğiniz kişinin sıra numarasını girin.: '))
                L.remove(L[kim-1])
                # print(f'{i+1}. {L[i]}')
            elif sil == 'h':
                print('Silme işlemi iptal')
        else:
            print('Listede kimse yok')
    elif isim == 'bitti':
        print('Restoranımız Kapandı')
        break