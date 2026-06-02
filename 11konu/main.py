import requests

""" 
HTTP Metotları (GET, POST, PUT, PATCH, DELETE) 

requests.get()      -> Veri Çekmek için Kullanılır.
requests.post()     -> Veri göndermek için kullanılır.
requests.put()      -> Veri Güncellemek için kullanılır.
requests.patch()    -> Veri Güncellemek için kullanılır.
requests.delete()   -> Veri Silmek için Kullanılır.
"""

url = 'https://jsonplaceholder.typicode.com/users'      ## Json verilerinin olduğu adres
jsonVeri = requests.get(url)                            ## Json dosyasından verileri çekti ve jsınVeri değişkenine atadı

## print(jsonVeri.status_code) ##200 sonucunu dönmeli

veriler = jsonVeri.json()   ## Json'dan gelen bilgileri obje/liste dataya dönüştürür.
## print(veriler)           ## Json datadan gelen tüm veriyi yazar.

print(f'Uzunluk: {len(veriler)}')

# Tek veri yazdırma
# print(veriler[0]["username"])

# Tüm Verileri Yazdırma
# for veri in veriler:
#     print(veri['username'])

# İlk 5 Veriyi Yazdırma
# for i in range(5):
#     print(veriler[i]['name'])

# Belirli bir aralıktaki veriyi yazdırma
for i in range(2,5):    #İndis2'den başlayıp indis4'e kadar yazdırır. indis5 dahil değildir.
    print(veriler[i]['name'])


""" 
POST metodu ile veri gönderme 
requests.post('veri gönderilecek json adresi', 'Gönderilecek Veri')
"""
veri = {
    "name":"Hayko",
    "surname":"Cepkin"
}

res = requests.post(
    'https://jsonplaceholder.typicode.com/users',
    json=veri
)

print(res) 