import random
L = ['python','print','random','while','choise']
kelime = random.choice(L)
adam =  ['''
    +----+
    o    |
   /|\   |
   / \   |
        ---''','''
    +----+
    o    |
   /|\   |
   /     |
        ---''','''
    +----+
    o    |
   /|\   |
         |
        ---''','''
    +----+
    o    |
   /|    |
         |
        ---''','''
    +----+
    o    |
    |    |
         |
        ---''','''
    +----+
    o    |
         |
         |
        ---''','''
    +----+
         |
         |
         |
        ---''']

dogruHarf = []
yanlisHarf = []
hak = len(adam)

while hak > 0:
    out = ''
    for h in kelime:
        if h in dogruHarf:
            out += h
        else:
            out+='_'
    if out == kelime:
        break
    print(f'Kelime: {out}')
    print(adam[hak-1])
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print(f'{girHarf} zaten girildi')
    elif girHarf in kelime:
        print('Doğru Harf')
        dogruHarf.append(girHarf)
    else:
        print('Yanlış Harf')
        hak-=1
        yanlisHarf.append(girHarf)

if hak != 0:
    print(f'Tebrikler. Kazandınız. {kelime}')
else:
    print(f'Maalesef. Kaybettiniz. {kelime}')