### Tahmin Oyunu ###
import random

sayi = random.randint(1,6)
tahmin = int(input('Tahmininizi Girin.: '))
skor = 5
while True:
    if(sayi == tahmin):
        print(f'Tahmin Doğru. Skorunuz: {skor}')
        break
    else:
        skor -= 1
        if(tahmin < sayi):
            print(f'Yukarı!! Tekrar Deneyin. Skorunuz: {skor}')
            tahmin = int(input('Tahmininizi Girin.: '))
        else:
            print(f'Aşağı!! Tekrar Deneyin. Skorunuz: {skor}')
            tahmin = int(input('Tahmininizi Girin.: '))