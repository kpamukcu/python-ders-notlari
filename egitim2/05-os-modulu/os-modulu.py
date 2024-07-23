""" 

os modülü genel olarak işletim sistemi ile ilgili bilgiler üzerinde sonuçlar üretir.

result = dir(os)
print(result)

"""

import os

result = os.name        #İşletim sistemi bilgisini verir (nt değeri windows işletim sistemi olduğunu beliertir.)
result = os.getcwd()    #Şuanki dosya ile ilgili hangi dizinde olduğu bilgisini verir.
##os.mkdir('yeni-klasor') #Dosyanın içinde olduğu dizin içinde Yeni klasör oluşturmayı sağlar. Ancak farklı bir dizinde klasör oluşturulması istenilirse chdir('c:\\') gibi dizin yolu değiştirilmelidir.

# os.chdir('C:\\') # Dizin yolunu değiştirebiliriz.
# os.mkdir('python-ile-klasor')

# os.chdir('..') # Dizin yolunu üst klasör olarak seçer. ../.. kullanılırsa 2 kere üst klasöre çıkmış olur.
# result = os.getcwd() #etin olan dizini verir


os.chdir('C://users/kaan.pamukcu/desktop') #dizin olarak masaüstüne geçiş yapıldı
os.makedirs('yeniKlasor/altKlasor') #masaüstünde yeniKlasor isimli klasör ve onun içine de altKlasor diye klasör açıldı.


print(result)