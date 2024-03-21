'''
DÖNGÜLER(LOOP)

- Tekrarlanması istenilen işlemler için kullanılırlar.
- For ve While olmak üzere iki döngü tipi vardır.,
- For döngüsünün döngü sayısı önceden bellidir.
- While döngüsünün döngü ayısı önceden belli olmayıp koşula bağldır. Örneğin space tuşuna basılan kadar ekrana adını yazdır.
- Bir liste içinde bir parametrenin olup olmadığını kontrol edebilmek için in ve not in operatörleri kullanılır. True ya da false sonucu döndürür.
- range(x,y) -> Sayı üretmek için, istenilen aralıkta sayı dizisi oluşturabilmek için kullanılır. Aynı zamanda for döngü yapısında çalışacak döngü sayısını belirlemek için kullanılır. x parametresi başlangıç değeri olup y parametresi ise döngünün sonlanacağı değerdir.
    
Sytax:
    for a in range(x,y):
        Yapılacak işlemlerin kodları gelecek

LİSTELER(List)

- Diğer dillerdeki array(), dizilere denk gelen özelliktir.
- Liste'ler tüm veri türlerini içinde barındırabilir.
- Liste'lerin içerdiği parametrelerin indexNo'ları mevcut olup ilk parametrenin indexNo'su sıfırdır.
'''

liste = ['Ali','Can','Miray','Zeynep']
print(liste)        #Ekrana ['Ali','Can','Miray','Zeynep'] yazar
print(liste[0])     #Ekrana Ali yazar

liste2 = 'Python'
print(liste2[1])    #Ekrana y yazar

print('Ali' in liste)   #Ekrana true sonucunu döndürür

#Rezervasyon ve Masa No kontrol uygulaması

isim = input('İsminiz Nedir? ')

masaNo = 0
if isim == 'Ali':
    masaNo = 5
if isim == 'Can':
    masaNo = 7
if isim == 'Miray':
    masaNo = 9
if isim == 'Zeynep':
    masaNo = 10


if isim in liste:
    print(f'Rezervasyonunuz Bulunmaktadır. Masa No: {masaNo}')
else:
    print('Rezervasyonunuz Yoktur.')


range(0,5)      #range(5)'te aynı sonucu verecektir. 0,1,2,3,4,5
range(11,6)     #11,10,9,8,7,6
range(1,10,2)   #1,3,5,7,9 değerleri 2'şer 2şer arttırarak ilerledi
range(15,7,-4)  #15,11,7 değerleri 4'er azaltarak ilerler

for a in range(0,5):
    print(a)

#Ör: 1'den 30'a kadar tek ayıları yazdıran uygulama

#1.Yöntem
for a in range(1,30,2):
    print(a)

#2.Yöntem
for b in range(1,30):
    if b%2==1:
        print(b)


##### While Döngüsü #####
### Ör: Sıfırdan farklı olduğu sürece girilen sayıların karesini alan program
        
x=1
print('Çıkmak için 0\'a Basın')

while(x!=0):
    x = int(input('Bir Sayı Girin'))
    print(x**2)
print('0\'a basarak çıkış yaptınız')