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

# input() -> Kullanıcıdan bilgi almak için kullanılır. input'tan alınan veriler her zaman string döner.
# float() -> input'tan alınan veriyi sayısal değere döndürür.
boyCm = float(input('Boy Bilginizi cm cinsinden girin'))
kg = float(input('Kilo Bilginizi Girin: '))

boyM = boyCm / 100
vki = kg / (boyM * boyM)
print(vki)


### Koşullu İfade Kullanımı ###
### if - elif - else
""" 
18.5 altı → Zayıf
18.5 – 24.9 → Normal
25 – 29.9 → Fazla kilolu
30+ → Obez 
"""
if vki < 18.5:
    print('Zayıfsınız')
elif vki < 25:
    print('Normal Kilodasınız')
elif vki < 30:
    print('Fazla Kilolusunuz')
elif vki >= 30:
    print('Obezite')
else:
    print('Vki Değeri Hesaplanamadı')


### Fonksiyon Kullanımı ###
def bmiHesapla(boyCM, kiloKg):
    boyM = boyCM / 100
    return kiloKg / (boyM * boyM)

def bmiYorum(vkin):
    if vkin < 18.5:
        return 'Zayıf'
    elif vkin < 25:
        return 'Normal'
    elif vkin < 30:
        return 'Kilolu'
    else:
        return 'Obezite'


boyunuz = float(input('Cm cinsinden boyunuzu Girin: '))
kilonuz = float(input('Kg Cinsinden Kilonuzu Girin: '))

endeks = bmiHesapla(boyunuz,kilonuz)
yorum = bmiYorum(endeks)

print('VKI Değeriniz: ', endeks )
print('VKI Yorum: ', yorum)