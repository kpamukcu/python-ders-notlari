import random

#result = dir(random)    #random modülü içindeki fonksiyonları yakalar
#result = help(random)   #random modülü içindeki fonksiyonların kullanım ayrıntılarını verir.


result = random.random()    # 0.0 ile 1.0 arasında rastgele bir sayı üretir. (0.0 ve 1.0 dahil)
result = random.uniform(1,10)   # 1.0 ile 10.0 arasında rastgele bir sayı üretir. 
result = int(random.uniform(10,100)) #10 ile 100 arasında float olarak üreilen sayının sadece tam sayı kısmını üretir.
result = random.randint(100,150) #100 ile 150 arasında rastgele tam bir sayı üretir.

name = ['ali','yağmur','deniz','cenk']
result = name[random.randint(0,3)] #0 ile 3 arasında rastgele tam bir sayı üretip indisNo olarak kullanır ve name listesinden ilgili parametreye ulaşır.
result = name[random.randint(0,len(name)-1)] #0 ile name listesinin uzunluğundan 1 çıkararak bulunun değer ile arasında rastgele tam bir sayı üretip indisNo olarak kullanır ve name listesinden ilgili parametreye ulaşır.
result = random.choice(name)    #name listesi içinden bir parametreyi rastgele seçer

liste = list(range(10)) #range ile 0'dan 9'a kadar 10 adet sayı üretir ve list fonksiyonu ile listeye dönüştürür.
print(liste) #ekrana [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] yazar

random.shuffle(liste) #shuffle -> Liste içindeki parametlerin sırasını rastgele karıştırır.
print(liste)

liste = range(100)
result = random.sample(liste,3) #sample -> liste içinden rastgele 3 parametre yakalar.
result = random.sample(name,2)  #name dizisi içinden rastgele 2 isim getirir
print(result)