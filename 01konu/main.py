"""
String ve String Metotları

Metinsel verileri ifade eden data türüdür. Tırnak içinde yazılırlar.

    Metot           Amaç                                        Açıklama
1-  lower()         Küçük harf Dönüştürür.                      Özellikle kullanıcı girişleri için. Ör: Mail Adresi girişi
2-  upper()         Büyük harfe dönüştürür.                     Özellikle kullanıcı girişleri için
3-  title()         İlk Harfleri Büyütür.                
4-  capitalize()    Sadece ilk harfi büyütür.
5-  strip()         Baştaki ve Sondaki Boşlukları Siler         Kullanıcın hatalı olarak boşluk eklemesi ihtimali 
6-  lstrip()        Soldaki Boşlukları Siler                    Kullanıcın hatalı olarak boşluk eklemesi ihtimali
7-  rstirp()        Sağdaki Boşlukları Siler                    Kullanıcın hatalı olarak boşluk eklemesi ihtimali
8-  find()          Kelimenin indexNo'sunu verir                Arama İşlemleri için kullanılır. Bulursa indexNo verir yoksa -1 döner. Ör: "@" işareti var mı?
9-  index()         Kelimenin indexNo'sunu verir                Arama İşlemleri için kullanılır. Bulursa indexNo verir yoksa hata döner. 
10- startswith()    Şununla mı Başlıyor                         Dosya kontrolleri için. ör: "htmls://" var mı?                   
11- endswith()      Şununla mı Bitiyor                          Ör: .exe var mı?
12- replace(x,y)    Metni Değiştir                              x değişecek kelime y yeni kelime parametreleridir. 
                                                                Ör: 0555-555-55-55 formatını 05555555555 değiştirir.
                                                                Ör: Seo Uyumlu Url Yapılabilir. "Python 2026 Dersleri" <-> "python-2026-dersleri"

13- split()         Metni Listeye Böler                         Her Kelimeyi parçalayıp liste dataya dönüştürür. Karaktere göre parçalama da yapar.
                                                                Ör: csv verisi işlerken kullanılabilir

                                                                
14- isalpha()       Sadece harf mi kontrolü yapar               İfade içinde sadece harf olup olmadığını kontrol eder.
                                                                Ör: Form validation'larında kullanılır. "Sadece Harf Girin" 

15- isdigit()       Sadece sayı mı kontrolü yapar               İfade içinde sadece sayı olup olmadığını kontrol eder.
                                                                Ör: Form validation'larında kullanılır. "Sadece Sayı Girin"

16- isalnum()       Harf + Sayı mı?                             İfade içinde sadece sayı ve harf olup olmadığını kontrol eder.
17- islower()       Küçük Harf mi kontrolü yapar
18- isupper()       Büyük harf mi kontrolü yapar
19- len()           Metinin karakter uzunluğunu verir.          Ör: Şifre giriş uzunlukları

"""


metin1 = 'BU METİN BÜYÜK HARF Mİ KÜÇÜK HARF Mİ?'
print(metin1.lower())

metin2 = 'bu metin küçük harf mi büyük harf mi?'
print(metin2.upper())

metin3 = 'mETnin hAnGi harFlerİ bÜYÜK'
print(metin3.title())

metin4 = 'METNİN İLK KELİMESİNİN İLK HARFİ NE BÜYÜK MÜ?'
print(metin4.capitalize())

metin5 = '       @pamukcukaan       '
print(metin5.strip())

metin6 = '    @aribilgi     '
print(metin6.lstrip())

metin7 = '    @acibadem    '
print(metin7.rstrip())

metin8 = 'Bu metnin içinde LOREM var mı?'
print(metin8.find('LOREM'))
print(metin8.find('v'))
print(metin8.find('@'))             # -1 sonucunu verir
print(metin8.index('var'))
# print(metin8.index('@'))          # Hata Döner ve Proje Durur

metin9= 'https://kaanilepythondersleri.com'
print(metin9.startswith('https://'))        #true döner
print(metin9.endswith('.com'))              #true döner
print(metin9.endswith('.org'))              #false döner

metin10='0555-555-55-55'
print(metin10.replace('-',''))

metin11 = 'Hayko Bülent Mahmut Yıldız Ajdar Aleyna'
print(metin11.split())
metin12 = 'Hayko Cepkin, Bülent Ersoy, Mahmut Tuncer, Yıldız Tilbe, Ajdar, Aleyna Tilki'
print(metin12.split(','))

metin13 = 'pythondersleri2026'
print(metin13.isalpha())        #metin13 içinde sayı olduğu için false döner
print(metin13.isdigit())        #metin13 içinde harf olduğu için false döner
print(metin13.isalnum())        #metin13 içinde hem harf hem de sayı içerdiği için true döner

metin14 = 'PYTHONDERSLERI@GMAIL.COM'
print(metin14.islower())        #metin14 büyük harfler olduğu için false döner
print(metin14.isupper())        #metin14 büyük harfler olduğu için true döner


### Örnek:
### Üyelik İşlemi ###
kadi = input('Mail Adresinizi Girin: ').strip().lower()
sifre = input('Şifrenizi Girin ör:123456: ').strip()

if '@' in kadi and sifre.isdigit() and '.com' in kadi:
    uye = f'{kadi},{sifre}'
    print(uye.split(','))
else:
    print('Format Hatası Yaptınız')