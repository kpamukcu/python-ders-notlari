### Kütüphane Üyelik Uygulaması

kitap = {
    1 : 'Yüzüklerin Efendisi',
    2 : 'Kürk Mantolu Madonna'
}

u ={}

# while True:
    # islem = input('Lütfen İşlem Seçin.: Yeni Kayıt (Y) - Bilgi (B) - Sil (S) - Kitap Ekle (Ke) ').capitalize()

    # if islem == 'Y':
    #     uyeSayisi = len(u)
    #     tc = input('Yeni Üye Kimlik No.: ')
    #     u[tc] = {}
    #     u[tc]['isim'] = input('Yeni Üye Adı Soyadı.: ')
    #     u[tc]['tel'] = input('Telefon Numarası.: ')
    #     u[tc]['adres'] = input('Adres Bilgisi.: ')
    #     u[tc]['kno'] = int(input('Aldığı Kitap No.: '))
    #     print(u)
    # elif islem == 'B':
    #     uyeBul = input('Üye Tc Kimlik No.: ')
    #     uye = u.get(uyeBul, False)
    #     if uye == False:
    #         print(u.get(uyeBul,'Kayıt Yok'))
    #     else:
    #         print(f'Ad Soyad: {u[uyeBul]['isim']}')
    #         print(f'Telefon: {u[uyeBul]['tel']}')
    #         print(f'Adres: {u[uyeBul]['adres']}')
    #         print(f'Kitap: {kitap[u[uyeBul]['kno']]}')
    # elif islem == 'S':
    #     uyeSil = input('Üye Tc Kimlik No.: ')
    #     u.pop(uyeSil)
    # elif islem == 'Ke':
    #     kitapSay = int(len(kitap))
    #     kitap[kitapSay+1] = input('Yeni Kitap Adını Girin')
    #     print(kitap)

kitapList = {}
uyeList ={}

while True:
    islem = input('Lütfen İşlem Seçin \nÜyelik İşlemleri (1) - Kitap İşlemleri (2) - Çıkış Yap (ç).: ')

    #Üyelik İşlemleri
    if islem == '1':
        uyeIslem = input('Yeni Kayıt(1) - Bilgi Güncelle(2) - Üye Listesi (3) - Üye Sil(4) ')

        #Yeni Üye Kaydetme
        if uyeIslem == '1':
            tc = input('Üye Tc Kimlik No Girin.: ')
            uyeList[tc] = {}
            uyeList[tc]['isim'] = input('Üye Ad Soyad.: ')
            uyeList[tc]['telefon'] = input('Telefon No.: ')
            uyeList[tc]['adres'] = input('Adres.: ')
            uyeList[tc]['kitaplar'] = input('Kitap No Girin.: ')
            print('Yeni Üye Kaydı Tamamlandı')
        
        #Üye Kaydı Güncelleme
        elif uyeIslem == '2':
            while True:
                tc = input('Üye Tc Kimlik No Girin.: ')
                uyeBul = uyeList.get(tc,False)
                
                if uyeBul == False:
                    print('Üye Kaydı Bulunamadı')
                else:
                    while True:
                        print('Güncelleme işlemini bitirmek için ç yazın')
                        guncelle = input('Güncellemek istediğiniz bilgiyi seçin İsim - Telefon - Adres - Kitaplar.: ')
                        if guncelle != 'ç':
                            uyeList[tc][guncelle] = input(f'{guncelle.capitalize()} Güncelleme.: ')
                            print('Üye Bilgileri Güncellendi')
                        else:
                            print(f'İsim: {uyeList[tc]['isim']}')
                            print(f'Telefon: {uyeList[tc]['telefon']}')
                            print(f'Adres: {uyeList[tc]['adres']}')
                            print(f'Kitaplar: {uyeList[tc]['kitaplar']}')
                            break
                    break
    elif islem == '2':
        kitapislem = input('Yeni Kitap Girişi (1) - Kitap Bilgi Güncelle (2) - Kitap Listesi (3) - Kitap Sil (4)')

        if kitapislem == '1':
            kNo = int(input('Kitap No Girin.: '))
            kitapList[kNo] = {}
            kitapList[kNo]['isim'] = input('Kitap Adını Girin.: ')
            kitapList[kNo]['yazar'] = input('Yazar İsmini Girin.: ')
            kitapList[kNo]['tur'] = input('Kitap Türünü Girin.: ')
            kitapList[kNo]['basim'] = input('Basım Tarihini Girin.: ')
            print(kitapList)
        