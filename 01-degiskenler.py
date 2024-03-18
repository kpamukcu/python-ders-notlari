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


'''


A=13
print(A)

isim = 'Kaan'
print(isim)

adiniz = input('Lütfen Adınızı Girin ')
print(adiniz)



