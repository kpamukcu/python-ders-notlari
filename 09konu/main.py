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



"""

import requests

response = requests.get('https://acibademmobil.com.tr')
print(response.status_code)                                 ##İlgili web sitesinin statü kodunu verir.

print(requests.get('https://aribilgi.com').status_code)     ##İlgili web sitesinin statü kodunu verir.
# print(response.text)                                        ##İlgili web sayfasının kaynak kodlarını yakalar.


if response.status_code == 200:
    print('Site Yayında')


##Veri Çekme
jsonApi = requests.get('https://dummyjson.com/products')
data = jsonApi.json()
print(data['products'][0]['title'])

##Parametre Gönderme
import requests

parametreler = {
    "q" : "python",
    "sort" : "stars"
}

response = requests.get('https://api.github.com/search/repositories',params=parametreler) 
##Url Aslında https://api.github.com/search/repositories?q=python&sort=stars şeklinde get isteği atmış olur

print(response.json())

##Post request (Veri Gönderme)
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

