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

file = open('newfile.txt','r',encoding='utf-8')

### For Döngüsü ile Okunan değerleri yazdırma
# for i in file:
#     print(i, end="") #eğer end="" eklenmezse her bir satır arasına boş bir satır daha ekler
# file.close()

# read() fonksiyonu ile
content = file.read()
print(content) #Tüm içeriği satır satır boş satır eklemeden yazar. 