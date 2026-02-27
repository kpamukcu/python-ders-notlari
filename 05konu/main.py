""" 
Koşullu İfadeler (if - elif - else)

- Birden fazla durumu karşılaştırmak için kullanılırlar.
- Bir veya birden fazla koşulun gerçekleşmesi ve gerçekleşmemesi durumuna göre kara veren yapıladır.

if -> Bir koşulun gerçekleşmesi durumunda çalışacak kod kümesi
elif -> İkinci veya diğer koşullardan birinn gerçekleşmesi halinde çalışacak kod kümesi
else -> Hiç bir koşulun gerçekleşmemesi halinde çalışacak kod kümesi

if KOŞUL:
    Koşul Gerçekleşmesi Halinde Çalışacak Kodlar Burada
elif DİĞER_KOŞUL1:
    Diğer_Koşul1 Gerçekleşmesi Halinde Çalışacak Kodlar Burada
elif DİĞER_KOŞUL2:
    Diğer_Koşul2 Gerçekleşmesi Halinde Çalışacak Kodlar Burada
else:
    Hiçbir koşulun gerçekleşmemesi halinde çalışacak kodlar burada


Çalışma Mantığı
1- İlk if kontrol edilir
2- Doğruysa → durur
3- Yanlışsa → eliflere bakar
4- Hiçbiri doğru değilse → else çalışır

İlk doğru olan blok çalışır, diğerlerine bakılmaz.

Koşullarda Kullanılan Operatörler
==      -> Eşittir
!=      -> Eşit Değildir
>       -> Büyüktür
<       -> Küçüktür
>=      -> Büyük Eşittir
<=      -> Küçük Eşittir
and     -> ve anlamına gelir. Aynı anda birden fazla durumun doğru olması gerekir
or      -> veya anlamına gelir. Aynı anda birden fazla durumun bir tanesinin doğru olması yeterlidir.
not     -> değil anlamına gelir. Koşulun yanlış olması anlamına gelir.


Ternary (Tek Satırlı Koşullu İfade)
deger_if_true if kosul else deger_if_false

Ör: sonuc = "A" if kosul else "B"

 """

### Sertifika Puan Kontrolü
puan = 69

if puan >=90:
    print('Tebrikler Başarı Sertfikası Aldınız. Puanınız: ', puan)
elif puan >= 70:
    print('Puanlı Katılım Sertifkası Aldınız. Puanınız: ', puan)
else:
    print('Katılım Sertifikası Aldınız. Puanınız: ', puan)


### Ehliyet Başvuru Kontrolü

dogum = input('Doğum Yılınızı Girin: ')
yas = 2026 - int(dogum)

if yas >= 18:
    print(f'{yas} yaşındasınız. Ehliyet Başvurusu Yapabilirsiniz.')
else:
    print(f'{yas} yaşındasınız. {18-yas} yıl sonra ehliyet başvusuru yapabilirisiniz.')


## Kullanıcıdan bir sayı alın ve çift ya da tek sayı olup olmadığını kontrol edin.
sayi = int(input('Bir Sayı Girin: '))

if sayi % 2 == 0:
    print(f'Girdiğiniz {sayi} sayısı çifttir.')
else:
    print(f'Girdiğiniz {sayi} sayısı tekdir.')


""" 
Kullanıcıdan bir sayı al.

Durum1: Sayı pozitif çift
Durum2: Sayı pozitif tek
Durum3: Sayı negatif çift
Durum4: Sayı negatif tek
Durum5: Sayı 0
"""

yeniSayi = int(input('Bir Sayı Giriniz: '))

if yeniSayi >0 and yeniSayi%2 == 0:
    print(f'{yeniSayi} pozitif ve çift sayıdır')
elif yeniSayi > 0 and yeniSayi%2 != 0:
    print(f'{yeniSayi} pozitif ve tek sayıdır.')
elif yeniSayi < 0 and yeniSayi%2 == 0:
    print(f'{yeniSayi} negatif ve çift sayıdır.')
elif yeniSayi <0 and  yeniSayi%2 !=0:
    print(f'{yeniSayi} negatif ve tek sayıdır.')
else:
    print('Sayı 0')

### Alternatif Çözüm - Nested IF (iç içe if kullanımı)
# Önce pozitif/negatif ayrımı yapıyoruz
# Sonra çift/tek kontrol ediyoruz
# Daha az tekrar var
# Okunabilirlik daha yüksek

yeniSayi2 = int(input('Bir Sayı Giriniz: '))

if yeniSayi2 > 0:
    if yeniSayi2 % 2 == 0:
        print(f'{yeniSayi2} pozitif ve çift sayıdır')
    else:
        print(f'{yeniSayi2} pozitif ve tek sayıdır')

elif yeniSayi2 < 0:
    if yeniSayi2 % 2 == 0:
        print(f'{yeniSayi2} negatif ve çift sayıdır')
    else:
        print(f'{yeniSayi2} negatif ve tek sayıdır')

else:
    print('Sayı 0')


# Sayıyı sadece bir kez %2 ile kontrol ederek
# ve sadece bir kez pozitif/negatif kontrol ederek
# en profesyonel çözüm

yeniSayi3 = int(input('Yeni Bir Sayı Giriniz: '))

if yeniSayi3 == 0:
    print("Sayı 0")
else:
    if yeniSayi3 % 2 == 0:
        tip = "çift"
    else:
        tip = "tek"
        
    if yeniSayi3 > 0:
        durum = "pozitif"
    else:
        durum = "negatif"
        
    print(f"{yeniSayi3} {durum} ve {tip} sayıdır.")