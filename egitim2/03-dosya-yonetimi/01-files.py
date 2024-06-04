# Dosya açmak ve oluturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

""" 'w': (Write) yazma.  """
#   * Dosyayı konumda oluşturur.
#   * Dosya varsa içeriğini siler ve yeniden ekleme yapar.

# Aynı konumda Dosya Oluşturma
# file = open('newfile.txt','w') #Dosya olmadığı için ana konumda newfile.txt dosyasını oluşturdu.
# file.close() #close() ile açılan dosya kapatılır.

# Farklı bir konumda dosya oluşturma
# file = open('c:/users/kaan.pamukcu/desktop/newfile.txt','w')
# file.close()

# file = open('newfile.txt','w',encoding='utf-8')
# # file.write('Kaan Pamukçu')
# file.close()


""" 'a': (Append) ekleme. """
#   * Dosya konumda yoksa oluşturur.
#   * Cursor ilgili dosyada neredeyse yeni ifadeyi oradan ekler

# file = open('newfile.txt','a',encoding='utf-8')
# # file.write('Hakan Yılmaz')
# # file.write('\nMahmut Tuncer') #Yeni bir satır üzerine yeni ifadeyi ekler.
# file.write('Hayko Cepkin\n') #Her seferinde yeni bir satır oluşturur ve bir sonraki yazım işlemi o yeni satır üzerinde gerçekleşir.
# file.close()


""" x': (Create) oluşturma. """
#   * Dosya zaten varsa hata verir.

# file = open('newfile2.txt','x',encoding='utf-8')
# file = open('newfile2.txt','x',encoding='utf-8')


""" 'r': (Read) okuma. """
#   * Varsayılan bir moddur. r ataması yapılmasa bile read modu çalışır
#   * Dosya konumda yoksa hata verir.

# file = open('newfile.txt','r',encoding='utf-8')

### For Döngüsü ile Okunan değerleri yazdırma
# for i in file:
#     print(i, end="") #eğer end="" eklenmezse her bir satır arasına boş bir satır daha ekler
# file.close()

# read() fonksiyonu ile
# content = file.read()
# print(content) #Tüm içeriği satır satır boş satır eklemeden yazar. 

# read(size) fonksiyonu ile beliertilen kararkter sayına kadar ki kısmı okur
# content = file.read(6)
# print(content)

# readline() fonksiyonu ile her seferinde tek satır okur
# content = file.readline()
# print(content,end="") ### end="" ile boş satır getirmesi engellendi

#readlines() fonksiyonu ile her bir satırdaki elemanları liste(dizi) elemanına dönüştürür.
# liste = file.readlines() #parantez içinde girilen bir sayı ile liste içine kayıt edilmesi istenilen satır sayısını belirtmiş oluruz.
# print(liste)


#Okuma için çalıştırılan dosya işlmelerin sonunda file.close() ile kapatılmalıdır.
#file.close() ile kapatmaya gerek kalmadan with metodu ile kod kümesi içinde işlemleri yaptığımızda kapatma işlemine gerek kalmaz.

# with open('newfile.txt','r',encoding='utf-8') as file:
#     content = file.read()
#     print(content) #Ekrana 0123456789abcçdefgĞhıijklmnoöprsştuüvyz yazar
#     print(file.tell()) #Cursor'un kaçıncı karakterde olduğunu belirtir. (45)
#     file.seek(5) #cursorun kaçıncı karaktere gitmesi belirlenir.
#     print(file.tell()) #Cursor'un kaçıncı karakterde olduğunu belirtir. (5)


### Dosya güncelleme

# with open('newfile.txt','r+',encoding='utf-8') as file: #r+ hem okuma hem de yazma anlamına gelmektedir.
#     file.write('Deneme') #r+ moduna açıldığı için dosyadaki tüm bilgileri silip yenisini yazmak yerine string ifadeyi eskisinin önüne ekledi. Eğer w modunda açılsaydı eski bilgileri silip yenisini yazacaktı. Güncellemeyi istediğimiz bir konumdan yapmak için file.seek(x) metodu x yerine bir değer verilerek file.write()'tan önce kodlamak gerekir. 

# with open('newfile.txt','r+',encoding='utf-8') as file: #r+ hem okuma hem de yazma anlamına gelmektedir.
#     print(file.read())

### Sayfanın sonunda güncelleme
with open('newfile.txt','a',encoding='utf-8') as file: ## a modu append olduğu için cursor sayfanın son konumuna gelir. Güncelleme de böylelikle sayfanın sonuna gelmiş olur.
    file.write('\nBülent')
    file.write('\nAjdar')  

with open('newfile.txt','r',encoding='utf-8') as file:
    print(file.read())