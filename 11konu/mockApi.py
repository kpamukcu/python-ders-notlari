import requests

## Get ile Veri Ekleme
apiUrl = 'https://6a96c6a70e3240db90615e00.mockapi.io/urun'
data = requests.get(apiUrl)

## Statu Control
print(data.status_code)    ## Ekrana 200 vermeli

if data.status_code == 200:
    while(True):
        islem = input('Yapmak İstediğiniz İşlem: Y-> Yeni Kayıt, G-> Ürün Güncelle, D-> Ürün Sil, L-> Ürün Listesi, X-> Çıkış ..: ')

        if islem == 'Y':
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
        elif islem == 'G':
            print('Ürün Güncellendi')
        elif islem == 'D':
            print('Ürün Silindi')
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