#error => Hata

# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

#error handling => Hata yönetimi


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için 0 girilemez')
# except ValueError:
#     print('x ve y için sayısal bir değer girin')


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError):
#     print('Hatalı Giriş Yaptınız')


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print('Hatalı Giriş Yaptınız')
#     print(e) #Hata ile ilgili bilgi verecek


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Hatalı Giriş Yaptınız')


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Hatalı Giriş Yaptınız')
# else:
#     print('Herşey yolunda')

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except:
#         print('Hatalı Giriş Yaptınız')
#     else:
#         break


#### Raise Exception (Hata Oluşturma/Fırlatma) ####

# x = 10
# if x > 5:
#     raise Exception('x 5\'den büyük olamaz')


def check_password(psw):
    import re #Regular Expration modülü eklendi.
    if len(psw) < 8:
        raise Exception('Parola En Az 8 Karakter Olmalıdır.')
    
    elif not re.search('[a-z]', psw):
        raise Exception('Parola Küçük Harf İçermelidir.')
    
    elif not re.search('[A-Z]', psw):
        raise Exception('Parola Büyük Harf İçermelidir.')
    
    elif not re.search('[0-9]', psw):
        raise Exception('Parola Rakam İçermelidir.')
    
    elif not re.search('[_@$]', psw):
        raise Exception('Parola özel karakter içermelidir.')
    
    elif re.search('\s', psw):
        raise Exception('Parola boşluk içermemelidir.')
    
    else:
        print('Parola Onaylandı')


password = '12345678aB_'

try:
    check_password(password)
except Exception as es:
    print(es)
finally:
    print('İşlem Tamamlandı')