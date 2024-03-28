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