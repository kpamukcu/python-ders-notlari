""" 
Sözlükler (Dict)

1- Birden fazla data tutmak için kullanılırlar.
2- Dizilerden en büyük farkı indisNo yerine bizim belirleyeceğimiz key'ler ile oluşturulurlar
3- key:value ikilisi halindedir
    1.Yöntem
    degiskenAdi = {'key1': value1,'key2': value2,'key3': value3,'key4': value4}
    2.Yöntem
    degiskenAdi = dict([('key1',value1),('key2',value2),('key3',value3)])

4- Boş bir sözlük doldurma;
    s = {}
    s[key1] = 'value1'
    s[key2] = 'value2'

5- Bir sözlük içindeki bir key'in değerini yazdırmak için get() fonksiyonu kullanırız.
   Ör: sozlukAdi.get('keyAdi')

   Not: Eğer veriyi getiriken keyAdi ilgili sözlük içinde yer almıyorsa get() fonksiyonuna ikinci bir parametre tanımlayabilir o aranan key ve değeri yoksa ekra ikinci parametrede yazan ifadenin çıkması sağlanabilir.
   Ör: sozlukAdi.get('keyAdi','YOK')

6- Bir sözlük içindeki bir key ve value'sunu silmek için pop() fonksiyonu kullanılır.
   Ör: sozlukAdi.pop('keyAdi)

7- keys() fonksiyonu sözlük içindeki key'leri verir. sozlukAdi.keys()
8- values() fonksyionu sözlük içindeki value'ları verir. sozlukAdi.values()
9- items() fonkiyonu sözlük içindeki parametleri key:value ikilisi olarak dict fonksiyonu şeklinde verir
   dict([('key1',value1),('key2',value2),('key3',value3)])


Kümeler (set)

1- degiskenAdi = {value1, value2, value3,...} şeklinde tanımlanabilir
   degiskenAdi = set('value')

Demetler (tuple)
1- tuple'lar normal parantez ile tanımlanırlar.
   degiskenAdi = (value1, value2, value3,....)

Not: Tuple'ların parametreleri değiştirilemez. Bu durum da hafızada listelere göre daha az yer kaplamasını sağlar. Tupel'ları sözlüklerde key olarak kullanabiliriz.

"""

#1. Yöntem
mevsim = {'Kış': 1,'ilkbahar':2,'yaz':3,'sonbahar':4}

#2.Yöntem
TC = dict([('Hayko',1234),('Mahmut',2345),('Ajdar',3456)])

#Boş bir sözlüğe değer atama
S = {}
S['uye1'] = 'Hayko'
S['uye2'] = 'Mahmut'
S['uye3'] = 'Ajdar'
print(S)


appleStok = {'macbook':100, 'iwatch':150, 'iphone': 200}

print(appleStok.get('macbook')) #Ekrana 100 yazar
print(appleStok['macbook']) #Ekrana 100 yazar

print(appleStok.get('imac','yok')) #Ekrana yok yazacaktır.

appleStok.pop('iphone') #iphone key-value ikilisini sildi
print(appleStok) #Ekrana {'macbook': 100, 'iwatch': 150}

print(appleStok.keys()) #Ekrana dict_keys(['macbook', 'iwatch']) yazar
print(appleStok.values()) #dict_values([100, 150]) yazar
print(appleStok.items()) #Ekrana dict_items([('macbook', 100), ('iwatch', 150)]) yazar


### İNGİLİZCE SÖZLÜK UYGULAMASI ###
ara = input('Kelime Girin.: ')
TrEn = {
    'Pazartesi': 'Monday',
    'Salı': 'Tuesday',
    'Çarşamba': 'Wednesday',
    'Perşembe': 'Thursday',
    'Cuma': 'Friday',
    'Cumartesi': 'Saturday',
    'Pazar':'Sunday'
}

print(TrEn.get(ara, 'Kelime Bulunamadı'))



### Kümeler ###
k = {1,'Hakan','50'}
print(k)

k1 = {5,2,3,4,1}
k2 = {1,3,8,7,6}
k1k2 = k1 | k2 #İki kümeyi birleştirdik. ancak 1 ve 3 parametreleri ortak olduğu için yeni oluşan k1k2 kümesinde birer kere yazacak
print(k1k2) # ekrana {1, 2, 3, 4, 5, 6, 7, 8} yazar. artan sıralama ile görünecektir.

print(k1&k2) #iki kümenin kesişim değerlerini verir. Ekrana {1, 3} yazar.
print(k1-k2) #k1 kümesinde olup k2 kümesinde olmayanları gösterir. Ekrana {2,4,5} yazar.
print(k2-k1) #k2 kümesinde olup k1 kümesinde olmayanları gösterir. Ekrana {6,7,8} yazar.


### Demetler (tuple) ###
t = (1,'Hayko','*',325)
print(t) ## Ekrana (1, 'Hayko', '*', 325) yazar




