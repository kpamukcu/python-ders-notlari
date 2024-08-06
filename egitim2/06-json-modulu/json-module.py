""" 
Json data '' içinde dict syntax'ı ile gelecektir. 
Bu yapı string olarak çalıştığı için gelen datayı dict'e çevirmemiz gerekmektedir.
Bu data türü değişimini gerçekleştirebilmek için import json ile json modülünü yüklemek gerekiyor.

"""
#dictionary data türü
person = {
    'name':'Ali',
    'languages':['Python','C#']
}

result = person['name']
print(result) # Ekrana Ali yazar

result = person['languages']
print(result) # Ekrana ['Python','C#'] listesini getirecektir.

result = person['languages'][0]
print(result) # Ekrana Python yazar

### Json Kullanımı ###
import json
person_string = '{"name":"Ali", "languages":["Python","C#"]}'

#JSON String to Dict
result = json.loads(person_string) ##json.load ile string olan json'ı dict'e dönüştürüyor.

print(person_string)
print(result["name"])
print(result["languages"][1])


#harici bir json dosyasından veri okuma

with open("person.json") as f:
    data = json.load(f) #Harici bir json dosya içindeki json veriyi data değişkenine atadık

    print(data) #Json dosyasındaki tüm datayı dict şeklinde yazar
    print(data["name"]) #Ekrana Hayko Cepkin yazar


""" 
Json kaydetme işlemi 
Json kaydetme servisi üzerindn kaydetme işlemi yapılacak
Gönderme işlemi yapmadan önce objeyi json stringine çevirmek gerekiyor.
"""


#Dict to Json String
person_dict = {
    "isim":"Mahmut Tuncer",
    "languages":[
        "Html",
        "Css"
    ]
}

result = json.dumps(person_dict) #Obje datayı dönüştürüyoruz
print(result) #### Objeyi string olarak yazar
print(type(result)) #### data tipi olarak str yazar

with open('personJson.json', "w") as f:
    json.dump(person_dict, f) # oluşturulmuş dict(obje) nesnesini json olarak ilgili dosyaya yazdırdık