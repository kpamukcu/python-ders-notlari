import requests

""" 
HTTP Metotları (GET, POST, PUT, PATCH, DELETE) 

requests.get()      -> Veri Çekmek için Kullanılır.
requests.post()     -> Veri göndermek için kullanılır.
requests.put()      -> Veri Güncellemek için kullanılır.
requests.patch()    -> Veri Güncellemek için kullanılır.
requests.delete()   -> Veri Silmek için Kullanılır.
"""

""" 
GET metodu ile veri çekmek 
degiskenAdi = requests.get('json dosya adresi')
"""

url = 'https://jsonplaceholder.typicode.com/users'      ## Json verilerinin olduğu adres
jsonVeri = requests.get(url)                            ## Json dosyasından verileri çekti ve jsonVeri değişkenine atadı


"""
| Status Code                   | Kısa Açıklama                                      |
| ----------------------------- | -------------------------------------------------- |
| **200 OK**                    | İstek başarıyla işlendi.                           |
| **201 Created**               | Yeni bir kaynak/kayıt oluşturuldu.                 |
| **204 No Content**            | İşlem başarılı, ancak cevap verisi yok.            |
| **400 Bad Request**           | Gönderilen istekte hata var.                       |
| **401 Unauthorized**          | Kimlik doğrulama gerekli veya başarısız.           |
| **403 Forbidden**             | Kimlik doğrulandı ancak işlem için yetki yok.      |
| **404 Not Found**             | İstenen kaynak veya endpoint bulunamadı.           |
| **429 Too Many Requests**     | Çok fazla istek gönderildi; rate limit aşıldı.     |
| **500 Internal Server Error** | Sunucunun kendi içinde bir hata oluştu.            |
| **502 Bad Gateway**           | Sunucu, başka bir sunucudan geçerli cevap alamadı. |
| **503 Service Unavailable**   | Sunucu şu anda hizmet veremiyor.                   |
"""


print(jsonVeri.status_code) ##200 sonucunu dönmeli

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


#### mockAPI ile Canlı Örnek ####

url2 = 'https://6a3bcbf2e4a07f202e15e17e.mockapi.io/products'
data = requests.get(url)
print(f'mockApi sonuç: {data}')


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

print(res) ##201 response kodu dönmeli.


"""
PUT metodu ile veri güncelleme
requests.put('veri gönderilecek json adresi/idNo', 'Gönderilecek YENİ Veri')

Put Metodu ile bir kaydın tamamı güncellenir
"""


""" 
Request Headers (İstek Başlıkları)
Header ile API'ye ben kimim, hangi formatta bilgi gönderiyorum ve hangi bilgiyi istiyorum gibi ek bilgi iletmedir.
Kısaca HTTP isteğinin yanında gönderilen ek bilgilerdir.

import requests

headers = {
    "Content-Type":"application/json",          ## Gönderilen veri formatı
    "Accept":"application/json",                ## Beklenen veri formatı
    "Authorization": "Bearer ABC123"            ## Authorization kimlik, Bearer authentication şeması, ABC123 Token'dır
}

res = requests.post(
    "https://example.com/api/users",
    headers = headers
)


Not: Her API Bearer Token kullanmaz. Onun yerine X-API-Key kullananlar vardır.
"""

import requests

headers = {
    "Content-Type":"application/json",
    "Accept": "application/json"
}

veri = {
    "name":"Hayko",
    "yas":50
}

res = requests.post(
    'https://6a96c6a70e3240db90615e00.mockapi.io/urun',
    json=veri,
    headers=headers
)

if res.status_code == 201:
    print('Hayko Kayıt Edildi')