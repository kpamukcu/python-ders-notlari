import requests

#### GET ile Veri Çekmek ####
url = 'https://6a3bcbf2e4a07f202e15e17e.mockapi.io/products'
data = requests.get(url)
print(f'mockApi sonuç: {data}')
print(data.status_code)
print(data.json())

### POST ile Veri Göndermek ####

def addProduct():
    url = 'https://6a3bcbf2e4a07f202e15e17e.mockapi.io/products'
    durum = input('Ürün Eklemek İstiyor musunuz? ')
    if durum == 'y':
        name = input('Marka Adını Girin: ')
        price = int(input('Ücret Bilgisini Girin: '))
        stock = int(input('Stok Girin: '))

        newProduct = {
            'name':name,
            'price': price,
            'stock':stock
        }

        res = requests.post(
            url,
            json=newProduct
        )

        print(res.json())
    else:
        print('İşlem İptal Edildi')
        data = requests.get(url)
        print(data.json())

addProduct()



