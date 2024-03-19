'''

DEĞİŞKENLER

Metinsel ve/veya sayısal değerlerin atanması ile geçici olarak depolayan hafızalardır denilebilir. Atanan değerleri değiştirilebilir.

Ör: a = 5   -> a ibaderi değişken olup = karakteri ise atama operatörüdür. 5 ise a değişkenine atanan değerdir.

Değişken İsimleri Oluşturulurken Dikkat Edilmesi Gerekenler

1- Bir değişkenin isminin ilk karakteri ya harf ya da alt çizgi(_) ile başlamalıdır.
2- Bir değişken isminde alt çizgi haricinde boşluk veya diğer özel karakterler bulunmamalıdır.
3- Bir değişken ismi python komutu olamaz.

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    Bu listeyi bulabilmek için IDLE üzerinde import keyword yazdıktan sonra keyword.kwlist yazıp listelenebilir.

4- Python dili kabul etse de Türkçe karakterlerin kullanımı tercih edilmemelidir.
5- Büyük küçük harf duyarlılığı vardır yani A ile a farklı değişkenlerdir.


Özellikler
- Değişkenlerin değerleri birbirine aktarılabilir.
    A=5 ve B=7 şeklinde oluşturulan değişkenlerin değerlerini biririne aktarmak için A,B = B,A yazmak yeterlidir. Böylelikler A değişkenin değeri 7, B değişkenin değeri ise 5 olacaktır.

- Bir değişkene başlangıç değeri atanabilir.

'''


A=13
print(A)

isim = 'Kaan'
print(isim)

adiniz = input('Lütfen Adınızı Girin ') #input() -> Kullanıcıdan data almayı sağlar.
print(adiniz) 


#Değişkenleri Birbirine Aktarma

A=3
B=4
C=A #C'nin değeri 3'tür
A=B #A'nın değeri 4 oldu
B=C #B'nin değeri 3 oldu
print(A)

#Üstteki işlem 3 adımda gerçekleşti ancak bu işlemin kısa yolu mevcut olup A,B = B,A şeklinde yazılabilir.

k='BTK'
p='Akademi'

k,p = p,k

print(k) #Ekrana Akademi yazar
print(p) #Ekrana BTK yazar
print(p,k) #Ekrana BTK Akademi yazar

#Başlangıç Değeri
cep = 0
cep = cep + 10
cep = cep + 20
cep = cep + 25
cep = cep + 40
print(cep) #ekrana 95 yazacaktır.

