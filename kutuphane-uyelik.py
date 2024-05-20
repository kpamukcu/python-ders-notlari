### Üyelik Uygulaması

""" u = {
    'tc':{
        'isim': 'Kaan'
    }
}

print(u['tc']['isim']) """

kitap = {
    1 : 'Yüzüklerin Efendisi',
    2 : 'Kürk Mantolu Madonna'
}

u ={}

while True:
    islem = input('Lütfen İşlem Seçin.: Yeni Kayıt (Y) - Bilgi (B) - Sil (S) ').capitalize()

    if islem == 'Y':
        uyeSayisi = len(u)
        tc = input('Yeni Üye Kimlik No.: ')
        u[tc] = {}
        u[tc]['isim'] = input('Yeni Üye Adı Soyadı.: ')
        u[tc]['tel'] = input('Telefon Numarası.: ')
        u[tc]['adres'] = input('Adres Bilgisi.: ')
        u[tc]['kno'] = int(input('Aldığı Kitap No.: '))
        print(u[tc]['isim'])
        print(u)
    elif islem == 'B':
        uyeBul = input('Üye Tc Kimlik No.: ')
        print(f'Ad Soyad: {u[uyeBul]['isim']}')
        print(f'Telefon: {u[uyeBul]['tel']}')
        print(f'Adres: {u[uyeBul]['adres']}')
        print(f'Kitap: {kitap[u[uyeBul]['kno']]}')