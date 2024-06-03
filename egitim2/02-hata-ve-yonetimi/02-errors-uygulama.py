liste = ['1','2','5a','10b','abc','10','50']

# 1: Liste elemanları içindeki sayılsal değerleri bulun?
# 2: Kullanıcı q değerini girmedikçe aldığınız her input'un sayılsa bir değer olduğunda emin olun aksi halde hata mesajı versin
# 3: Girilen parola içinde türkçe karakter varsa hata versin


# 1: Liste elemanları içindeki sayılsal değerleri bulun?

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue    #Hata alındığında döngü devam etmesini sağlar.

# 2: Kullanıcı q değerini girmedikçe aldığınız her input'un sayılsal bir değer olduğunda emin olun aksi halde hata mesajı versin

# while True:
#     deger = input('Bir değer girin.: ')
#     if deger == 'q':
#         print('Çıkkış Yapıldı')
#         break
#     else:
#         try:
#             result = int(deger)
#             print('Sayılsal Giriş Yapıldı')
#             break
#         except Exception as ex:
#             print('Sayılsal değer girin')
#         finally:
#             print('İşlem Tamamlandı')


# 3: Girilen parola içinde türkçe karakter varsa hata versin

# turkce_karakterler = 'şçğüöıİ'

# parola = input('Parola: ')

# for i in parola:
#     if i in turkce_karakterler:
#         raise Exception('Türkçe Karakter Kullanmayınız')
#     else:
#         pass
# print('Geçerli Parola')
    