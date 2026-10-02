import requests

## Get ile Veri Ekleme
apiUrl = 'https://6a96c6a70e3240db90615e00.mockapi.io/urun'
data = requests.get(apiUrl)

## Statu Control
print(data.status_code)    ## Ekrana 200 vermeli

if data.status_code == 200:
    while(True):
        islem = input('Yapmak İstediğiniz İşlem: Y-> Yeni Kayıt, G-> Ürün Güncelle, D-> Ürün Sil, L-> Ürün Listesi, X-> Çıkış ..: ')

        if islem == 'Y':    ## Kayıt Ekleme POST
            product_name = input('Ürün Adını Girin: ')
            product_brand = input('Markayı Girin: ')
            product_price = int(input('Ürün Fİyatını Girin: '))

            yeniUrun = {
                "product_name" : product_name,
                "product_brand" : product_brand,
                "product_price" : product_price
            }

            res = requests.post(
                apiUrl,
                json=yeniUrun
            )
        elif islem == 'G': ## Kayıt Güncelleme PUT (Tüm Veriler)
            product_name= input('Güncel Ürün Adını Girin: ')
            product_brand= input('Güncel Marka Adını Girin: ')
            product_price= int(input('Güncel Ürün Fiyatını Girin: '))
            product_id= int(input('Ürün Kodunu Girin: '))

            urunGuncelle = {
                "product_name" : product_name,
                "product_brand" : product_brand,
                "product_price" : product_price,
                "id":product_id                
            }

            res = requests.put(
                f'{apiUrl}/{urunGuncelle["id"]}',
                json=urunGuncelle
            )

        elif islem == 'P':     ## Kayıt Güncelleme PATCH (Tek veya seçilen birçok veri)
            product_id = int(input('Ürün Kodunu Girin: '))
            product_price = int(input('Güncel Ürün Ücretini Girin: '))

            tekBilgiGuncelle ={
                "product_price": product_price
            } 
            res = requests.patch(
                f'{apiUrl}/{product_id}',
                json=tekBilgiGuncelle
            )
            print('Ürün Adı Güncellendi')
        elif islem == 'D': ## Kayıt Silme DELETE

            urunSil = int(input('Silmek İstediğiniz Ürün Kodunu Girin: '))

            res = requests.delete(
                f'{apiUrl}/{urunSil}',
            )

            if res.status_code == 200:
                print('Ürün Silindi')
            else:
                print('Bu ürün bulunamamıştır.')

        elif islem == 'L':
            urunListesi = data.json()
            for urun in urunListesi:
                for a,b in urun.items():
                    print(f'{a}: {b}')            
        elif islem == 'X':
            print('Çıkış Yapıldı')
            break
else:
    print('Database Hatası')

print(data.json())