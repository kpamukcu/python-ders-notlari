""" 
Request Kütüphanesi
Requests kütüphanesi, HTTP istekleri göndermek için kullanılan en popüler ve en kolay kütüphanelerden biridir.
Web siteleri, API’ler veya servislerle iletişim kurmak için kullanılır.

Requests ile şunları yapabilirsin:
    Bir web sayfasının içeriğini almak
    API'den veri çekmek
    Form verisi göndermek
    JSON veri almak veya göndermek
    HTTP header göndermek
    Cookie yönetmek
    Dosya upload etmek

Örnek Kullanım Alanları:

| Senaryo       | Açıklama                            |
| ------------- | ----------------------------------- |
| API kullanımı | Instagram, Twitter, hava durumu API |
| Web scraping  | Web sayfası içeriğini çekmek        |
| Otomasyon     | Botlar, veri çekme sistemleri       |
| Test          | API endpoint testleri               |



Request Kütüphanesi Kurulması Gerekmektedir.
    Terminal üzerinden "pip install requests" kodu ile request kütüphanesi python içine kurulur.
    Çalıştırabilmek için de py dosyası içinde "import requests" kod satırı ile yüklenir.


requests.get('https://siteadi.com')     -> Get isteği gönderir.
.status_code                            -> Web sayfasının statü kodunu verir.
.text                                   -> Web sayfasının kaynak kodlarını yakalar.


Requests'in En Çok Kullanılan Metotları
| Metot    | Açıklama         |
| -------- | ---------------- |
| get()    | veri almak       
| post()   | veri göndermek   |
| put()    | veri güncellemek |
| delete() | veri silmek      |
| patch()  | kısmi güncelleme |



"""

import requests

response = requests.get('https://aribilgi.com')
print(response.status_code)                                 ##İlgili web sitesinin statü kodunu verir.

print(requests.get('https://aribilgi.com').status_code)     ##İlgili web sitesinin statü kodunu verir.
# print(response.text)                                      ##İlgili web sayfasının kaynak kodlarını yakalar.

if response.status_code == 200:
    print('Site Yayında')

### ---------- ###
### Veri Çekme ###
### ---------- ###

jsonApi = requests.get('https://dummyjson.com/products')
data = jsonApi.json()
# print(data['products'][0]['title'])

##Parametre Göndererek Veri Çekme
parametreler = {
    "q" : "python",
    "sort" : "stars"
}

response = requests.get('https://api.github.com/search/repositories',params=parametreler) 
##Url Aslında https://api.github.com/search/repositories?q=python&sort=stars şeklinde get isteği atmış olur
## print(response.json())

### ---------------------------- ###
### Post request (Veri Gönderme) ###
### ---------------------------- ###

loginInfo = {
    "log": "kaan",
    "pwd": "ZorSifre789**",
    "wp-submit": "Log In",
    "redirect_to": "https://aribilgi.com/wp-admin/",
    "testcookie": "1"
}

res = requests.post('https://aribilgi.com/wp-login.php/', data=loginInfo)
print(res.status_code)
print(res.url)

### --------------- ###
### Header Gönderme ###
### --------------- ###
""" 
Bazı Api'lar veri gönderirken de veri çekerken de şifreli olabilir.

headers = {
    "Authorization": "Bearer TOKEN"
}
"""

headers = {
    "Authorization": "Bearer TOKEN"
}

response = requests.get('https://dummyjson.com/auth/login', headers=headers)

dummyRes = requests.get('https://raw.githubusercontent.com/kpamukcu/filmdata/refs/heads/main/film.json')
print(dummyRes.headers)

data = dummyRes.json()
print(data[0]['Title'])             ## Ekrana Avatar Yazar

for moviesName in data:
    print(moviesName['Title'])      ## Ekrana film isimlerini yazar


