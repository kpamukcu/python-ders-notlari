import requests

## GET Request ###
res = requests.get('https://httpbin.org/get')
print(res.status_code)              ##Ekrana 200 döner
print(res.text)

### POST Request ###
data = {
    "username":"hayko",
    "password":123
}

gonder = requests.post('https://httpbin.org/post',data=data)
print(gonder.json())

### POST Request 2 ###

oturum = requests.Session()

logInfo = {
    "kadi" : "smbl",
    "sifre" : "SembolMetal2023**"
}

login = oturum.post('https://sembolmetal.com/admin/',data=logInfo)

oturumInfo = oturum.get('https://sembolmetal.com/admin/dashboard.php')

print(oturumInfo.status_code)
print(oturumInfo.text[:500])