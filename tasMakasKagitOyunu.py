### TAŞ - KAĞIT- MAKAS Oyunu ###
import random
O = ['T','M','K']
R = random.choice(O)
S = input('Seçiminiz.: ').capitalize()

print(f'Bilgisayar {R} Seçti')
print(f'Sen {S} Seçtin')

if R == S:
    print('Berabere')
elif R == 'T' and S == 'M':
    print('Kaybettiniz')
elif R == 'T' and S == 'K':
    print('Kazandınız')
elif R == 'M' and S == 'T':
    print('Kazandınız')
elif R == 'M' and S == 'K':
    print('Kaybettiniz')
elif R == 'K' and S == 'T':
    print('Kaybettiniz')
elif R == 'K' and S == 'M':
    print('Kazandınız')
else:
    print('Geçersiz Giriş')