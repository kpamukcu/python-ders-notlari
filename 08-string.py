""" 
STRING

1) Metinsel değerleri ifade eder. Tek ya da çif tırnak arasında tanımlanırlar.
2) Boşlukta bir karakter olarak geçmekte olup herhangi bir rakam tırnak içinde yazılması halinde string data türüdür.
3) String değerlerde her bir karakterin indisNo'su(indexNo) vardır ve ilk karakterin indis nosu sıfırdır.
    ad = 'Hayko Cepkin' string değişkeninin 0 indexNo'lu karakteri H'dir.
4) insidNo'lar eksili indexler alabilir. bu durumda en son karakterden itibaren ilgili değere ulaşmış oluruz.
    ad = 'Mahmut Tuncer' string değişkeninin -1 indexNoİİ'lu karakteri r'dir.
5) String değerler + operatörü ile birleştirilebilir.
6) String değeri parçalamak için bir çok yöntem vardır
    a) degiskenAdi[:]  
    b) degiskenAdi[3:]      -> indexNo'su 3'ten itibaren olan kısım
    c) degiskenAdi[:3]      -> 3. karaktere kadar olan kısım
    d) degiskenAdi[1:5]     -> indexNo'su 1'den başlayarak 5. karaktere kadarki kısmı alır. Not: 5. kaakter dahil değildir.
    e) degiskenAdi[1::2]    -> indexNo'su 1'den başlayarak 2 karakter atlaya atlaya alır.
    f) degiskenAdi[1:6:3]   -> indexNo'su 1'den başlayarak 6. karaktere 3'er 3er atlayarak alır.
    g) degiskenAdi[::-1]    -> değerin tersten yazılmış halini verir

    Not: Bu dilimleme operatörleriyle string ifadenn tamamını veya bir kısmını silebiliriz. degiskenAdi[:-1] -> ilgili değerin son karakterini siler.

7) replace -> methodu ile güncelleme yapılabilir.
8) split('') -> metot'u ile bir ifadeyi belirlenen ayraca göre parçalayıp liste data türüme dönüştürebiliriz.
9) String bir değerin karakter sayısına ulaşabilmek için len() fonksiyonu kullanılır.
10) String bir değerin içindeki belirli bir karakterin sayısını öğrenebilmek için count() fonksiyonu kullanılır.
11) string değerleri karşılaştırmak için == ve is yöntemlerini kullanabiliriz.
12) String bir değerin içine degiskenAdi.format() ile dinamik bir değer eklenebiir.
13) String bir değeri ters çevirme -> ''.join(reversed(degiskenAdi))  Not: '' içine herhangi bir karakter yazılırsa string değeri tersten yazrken her karakter arasına tırnaklar arasına eklenen karakteri ekleyererek ekrana yazar.
    Kriptografi, Tarih formatının daha anlaşılır hale gelmesi için kullanılabilir.

14) degiskenAdi.lower()     -> ile string ifadenin tüm karaktrlerini küçük harfe çevirir.
    degiskenAdi.upper()     -> ile string ifadenin tüm karaktrlerini büyük harfe çevirir. 
    degiskenAdi.swapcase()  -> ile string ifadenin içindeki küçük harfleri büyük, büyük harfleri küçük harfe çevirir.
    degiskenAdi.capitalize()-> ile string ifadenin ilk harini büyük harfe çevirir.

15) 'bulunacakkKelime' in 'hedefKelime' -> Hedef kelime içinde buluncak kelime aranır olması halinde true yoksa false sonucunu verir.
    'bulunacakkKelime' not in 'hedefKelime' -> Hedef kelime içinde buluncak kelime aranır olmaması halinde true yoksa false sonucunu verir.    

"""

ad = 'Hayko Cepkin'
print(ad[3])    #Ekrana k yazacaktır.
print(ad[0])    #Ekrana H yazacaktır.
print(ad[-1])   #Ekrana n yazacaktır.
print(ad[-5])   #Ekrana u yazacaktır.

#String değerleri birleştirme
x= 'A'
y= 'R'
z= 'I'
print(x+y+z) #Ekrana Arı Yazar

L = x+y+z
print(L) #Ekrana Arı yazar

a= 'Arı'
b= 'Bilgi'
c= a+b
print(c)    #Ekrana ArıBilgi yazar.


S= 'Python'
S2 = S[:3]+'T'+S[4:]
print(S2) #Ekrana PytThon yazar


#String Güncelleme / Değiştirme
adres = 'Sultangazi-İstanbul'
adres2 = 'Kadıköy' + adres[10:]
print(adres2)

adres3 = adres.replace('İstanbul','İzmir') #Not: replace ile güncelleme yapılan işlemin değişkene atanması gerekiyor
print(adres3)

#String ifadenin tamamını veya bir kısmını silme
yazi = 'Python'
print(yazi[:-1]) #n karaterini siler ve ekrana Pytho yazar

for a in range(1,len(yazi)):
    print(yazi[:-a]) #ekrana sırasıyla sondan başa doğru karakterleri silip tek tek yazar. Ancak en son P harfi ekranda görünecektir


#for döngüsü ile string ifadenin karakterlerine tek tek ulaşma

for d in 'btkakademi':
    print(d) #string ifadenin karakterlerini tek tek ekrana yazar.

#String bir ifadeyi liste'ye dönüştürmek
cumle = 'Kaan_ile_Python_Dersleri'
cumle = cumle.split('_') #değişkene atadığımız taktirde liste data türüne dönüşmüş halini print ile yazdırabiliriz. yada parçalama işlemini print() fonkiyonu parametre parantezi içinde konumlandırmalıyız.
print(cumle) #veya print(cumle.split('_')) kullanımı da ['Kaan', 'ile', 'Python', 'Dersleri'] aynı sonucu verir

adres = 'Esentepe Mah._2312 Sok._No:23_Daire:1_Sarıyer_İstanbul'
adresList = adres.split('_')
print(f'Mahalle.: {adresList[0]}')
print(f'Sokak.: {adresList[1]}')
print(f'No.: {adresList[2]}')
print(f'Daire.: {adresList[3]}')
print(f'İlçe.: {adresList[4]}')
print(f'İl.: {adresList[5]}')


#len() fonksiyonu ile karakter sayısı bulma
cumle = 'Merhaba Python Öğreniyorum'
print(len(cumle)) #Ekrana 26 yazacaktır. Not: Boşluklar da dahil.
print(cumle.count('a')) #Ekrana 2 yazacaktır. sadece karakter değil kelime de aratıp sayısı bulunabilir.

#Karılaştırma
print('Php' == 'Python') #Ekrana false yazar
print('JavaScript' is 'JavaScript') #Ekrana true yazar
print('Html' != 'Css') #Ekrana true yazar


#format() ile string bir değer içine dinamik dğer atama

a = 'ile'
metin = 'Ali {} Veli'
metin = metin.format(a)
print(metin) #Ekrana Ali ile Veli yzacaktır. değişken adı metin yerine başka birşey de belirlenbilirdi.

duzYazi = 'Bilişim Dersleri'
tersYazi = '/'.join(reversed(duzYazi))
print(tersYazi)

#Palidrom Uygulaması
kelimeGir = input('Kelime Girin.: ')
terseCevir = ''.join(reversed(kelimeGir))

if kelimeGir == terseCevir:
    print(f'Girdiğiniz {kelimeGir} kelimesi Palidrom bir kelimedir.')
else:
    print(f'Girdiğiniz {kelimeGir} kelimesi Palidrom bir kelime değildir.')
#Not: Ancak büyük küçük arf duyarlılığı olduğu için aynı kelime girilse bile harflerden birinin büyük yada küçük yazılması halinde false sonucu verecektir. Bunun çözümü için aşağıdaki büyük küçük harf dönüşüm metotları algoritmaya eklenebilir.
    
""" 
kelimeGir = input('Kelime Girin.: ')
kelimeGirKucuk = kelimeGir.lower()
print(kelimeGirKucuk)
terseCevir = ''.join(reversed(kelimeGirKucuk))

if kelimeGirKucuk == terseCevir:
    print(f'Girdiğiniz {kelimeGir} kelimesi Palidrom bir kelimedir.')
else:
    print(f'Girdiğiniz {kelimeGir} kelimesi Palidrom bir kelime değildir.')
"""

#Büyük, Küçük Harf değişimi

isim = 'HaYKoCEPkiN'
kucukHarf = isim.lower()
print(kucukHarf)

buyukHarf = isim.upper()
print(buyukHarf)

buyukKucukHarf = isim.swapcase()
print(buyukKucukHarf)


#String içinde başka bir string ifadeyi arama
metin = 'PythonÖğreniyoumYapayZekaiçin'
ara = 'Öğren'
print(ara in metin) #True sonucunu verecektir.
