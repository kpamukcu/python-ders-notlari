""" 
Listeler(List) ve Demetler(Tuple)
Özellikle veri bilimi, yapay zeka ve backend tarafında listeler çok önemlidir.


Listeler (List)
    - Birden fazla veriyi tek değişkende saklamayı sağlar.
    - Köseli parantez [] ile tanımlanır.
    - Değerleri değiştirilebilir yapıdadır. (Mutable)
    - Listelerde parametreler sıralıdır yani herbir değerin indexNo'su vardır. indexNo'lar sıfırdan başlar.
    - Liste içindeki bir parametreye ulaşmak için indisNo'su bilinmelidir. degiskenAdi[indisNo]
    - Tüm veri türlerini içinde barındırabilir.
    - Aynı değerler içinde yer alabilir.
    - Dinamik veriler için kullanımı tercih edilir.


Liste Metotları

    - append()  -> Listenin sonuna eleman ekler.
    - insert()  -> Belirli index'e parametre ekler.
    - remove()  -> Belirtilen değeri(parametreyi) siler.
    - pop()     -> index'e göre siler ve silinen değeri döndürür. 
    - clear()   -> Tüm listeyi temizler.
    - index()   -> Parametrenin indexNo'sunu verir.
    - count(parametre)  -> Bir değerin liste içinde kaç tane olduğunu verir.
    - sort()    -> liste içindeki parametreleri küçükten büyüğe doğru sıralar.
    - reverse() -> Listenin içindeki parametreleri terse çevirir.

----------------------------------------------------------------------

Demetler (Tuple)
    - Listelere benzer yapıdadır.
    - Parametreler değiştirilemez. (Immutable)
    - Parantez () ile tanımlanırlar.
    - Sabit veriler için kullanımı tercih edilir.
    - Performansı daha hızlıdır.


"""

##Listeler(list)

sayilar = [1,2,3,4,5]
isimler = ['Hayko Cepkin','Mahmut Tuncer','Bülent Ersoy']
karma = [1,'Python', 3.14, False]

print(sayilar)          ## Ekrana [1,2,3,4,5] yazar
print(sayilar[3])       ## Ekrana 4 yazar

isimler[2] = 'Ajdar'    ## indisNo'su 2 olan "Bülent Ersoy" parametresi "Ajdar" olarak değiştirildi.
print(isimler)          ## Ekrana ['Hayko Cepkin', 'Mahmut Tuncer', 'Ajdar'] yazar.

#Liste Metotları




# ------------------------ #


##Demetler (Tuple)
koordinat = (10795,75449)
print(koordinat[1])     ##Ekrana 75449 yazar.