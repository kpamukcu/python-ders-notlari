'''
VERİ İŞLEMLERİ

- Klavyeden yapılan her giriş data türü olarak str'dir.
- input()   -> Kullanıcıdan veri girişi aldımığımız komuttur.
- print()   -> İçerdiği parametleri ekrana yazdırmak için kullanılan koddur.
- sep=      -> Ayırıcı diyebiliriz. print() ile birden fazla parametreyi ekrana yazdırırken ekranda parametreler arası ayraç koymayı sağlar.
- end=('')  -> Kabuk ekranda imlecin ilgili print çıktısının altına değilde sonuna eklenmesini sağlar. Tırnakları içine str ibare alabilir.
- format()  -> Str ve değişkeni bir arada kullanabilmeyi sağlar.


Not: \n alt satıra indirme yapar. str olarak \ yazdırabilmek için \\ şeklinde kullanmalıyız

'''

isim = input('Adınız: ')
print(isim)
yas = input('Yaşınız: ')
print(yas)
print(type(yas))    #Veri Türü olarak str olacaktır.
yas = int(yas)      #Veri türünü str'den int'e çevirdi.
print(type(yas))    #Veri türü olarak int olacaktır.

print('Kaan Pamukcu','Yazılımcı', sep=' - ')

print('İş Yeriniz?', end=(' '))
firma = input() #Kullanıcının giriş yapabilmesi için akif olaak input imleci "İş Yeriniz?" print'inin sonunda görünecektir.

A=5
print('A..:',A)

#format() Kullanımı 1.Yöntem
print('a..: {0}'.format(A))

#format() Kullanımı 2.Yöntem
print(f'A={A}')

#print ile çizim :) -> Ekler dosyasındaki köpek görselini çiziyoruz
print(" _____\n/ * * \\\n \\ . /")

#Not Ortamalası Hesaplama Örneği
Y1 = int(input('1.Sınav Notunu Girin? '))
Y2 = int(input('2.SInıv Notunu Girin? '))
ort = (Y1+Y2)/2
print(ort)

#Yaş Hesaplama Örneği
dt = int(input('Doğum Yılınızı Girin.: '))
yas = 2024 - dt
print(f'Yaşınız: {yas}')