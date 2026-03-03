""" 
While Döngüsü
Koşul doğru olduğu sürece çalışna bir döngüdür.

Syntax
while koşul:
    Çalışacak Kod Burada Yazılır.

Genellikle Kullanım Mantığı
✔ Kullanıcıdan doğru veri alınana kadar
✔ Şifre doğru girilene kadar
✔ Menü sistemi

"""

i = 1

while i<=5:
    print(i)
    i += 1


user = ['hayko','123']

while True:
    kadi = input('Kullanıcı Adınızı Girin: ')
    sifre = input('Şifrenizi Girin: ')

    if kadi == user[0] and sifre == user[1]:
        print('Admin Paneline Hoş Geldiniz.')
        break
    else:
        print('Kullanıcı Adı ve/veya Şifreniz Hatalı. Lütfen Tekrar Deneyin')
    