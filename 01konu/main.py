### Print Fonksiyonu ve Değişken Tanımlama ###
print('Merhaba')

isim = 'Kaan'
dogum = 1982
yas = 2026 - dogum

print('Benim Adım:', isim)
print('Yaşım: ', yas)

### BMI - Vücut Kitle Endeksi Hesaplama ###
boy = 1.70
kilo = 66
bmi = kilo / (boy * boy)
print(bmi)

### Kullanıcıdan Bilgi Alma ###

# input() -> Kullanıcıdan bilgi almak için kullanılır.
# float() -> Integer değeri float değere dönüştürür.
boyCm = float(input('Boy Bilginizi cm cinsinden girin'))
kg = float(input('Kilo Bilginizi Girin: '))

boyM = boyCm / 100
vki = kg / (boyM * boyM)
print(vki)