# t1 = int(input('Birinci Sayıyı Giriniz.: '))
# t2 = int(input('İkinci Sayıyı Giriniz.: '))

# def topla(a,b):
#     print(a+b)

# topla(t1,t2)



# c1 = int(input('Çarpım için ilk sayıyı girin.: '))
# c2 = int(input('Çarpım için ikinci sayıyı girin.: '))

# def carp(a,b):
#     print(a*b)

# carp(c1,c2)


def oyun():
    import random
    O = ['T','M','K']
    R = random.choice(O)
    S = input('Seçiminiz.: ')

    while True:
        if R == S:
            print('Tekrar \n')
            S = input('Seçiminiz.: ')
        elif R == 'T' and S == 'M':
            print(f'Kaybettiniz. Rakibiniz {R} seçti')
            break
        elif R == 'T' and S == 'K':
            print(f'Kazandınız. Rakibiniz {R} seçti')
            break
        elif R == 'M' and S == 'T':
            print(f'Kazandınız. Rakibiniz {R} seçti')
            break
        elif R == 'M' and S == 'K':
            print(f'Kaybettiniz. Rakibiniz {R} seçti')
            break
        elif R == 'K' and S == 'T':
            print(f'Kaybettiniz. Rakibiniz {R} seçti')
            break
        elif R == 'K' and S == 'M':
            print(f'Kazandınız. Rakibiniz {R} seçti')
            break
        else:
            print('Geçersiz Giriş')
            S = input('Seçiminiz.: ')