""" 
Turtle modülü ile çizim uygulaması

1- Öncelikle import turtle ile modülün yüklenmesi gerekmektedir.
2- Çizim işlemi matematikten bildiğimiz koordinat sistemi üzerinde position ile olacaktır. Bulunduğumuz koordinatı bulamak için .position() veya .pos() metotu kullanılınır.
3- Ekranın herhangi bir konuma ulaşmak içi .goto() , .setposition() ve/veya .setpos() metotu kullanılır
4- Eğer poziyonu başalngıç noktasına getirmek istersek .reset() ve/veya .home() metotları kullanılabilir.
5- turtle.mainloop() ve/veya turtle.done() metotu, Grafik çizim ekranı kullanıcı X'den kapatan kadar açık kalmasını sağlar
6- setx() ve sety() metotu ile sadece x ve sadece y pozisyonlarını gündellemiş oluruz.
7- .forward() veya .fd() metotu ile ileri doğru doğrusal çizgi çizilebilir. 
8- .backward() veya .bk() metotu ile geriye doğru doğrulsal çizgi çizilebilir.
9- .right() ve/veya .rt() ile sağa dönmeyi sağlar. Değer olarak derece alır.
10- .left() ve/veya .lt() ile sola dönmeyi sağlar. Değer olarak derece alır.
11- .getshapes() metotu ile çizim aracımızın cursor simgesi listesini görebiliriz. (arrow, blank, circle, classic, square, triangle, turtel)
12- .hideturtle ile simge gizlenebilir.
13- .showturtel() metotu ile gizlenen simge tekrar görünür olacaktır. 
14- .pensize() metotu ile çizgi kalınlığı belirlenir.
15- .color('cizgiRengi','dolguRengi') metotu ile çizimin rengini belirleriz.
16- .begin_fill() metotu ile .color()'da tanımlanan dolgu rengi atanmış olacak doldurmayı bitirmek içinde end_fill() metotu kullanılmalı
17- .colormode(255) metotu eklendikten sonra .color(r,g,b) metotuna değer girerek ara veya ana renkleri oluşturabiliriz.


Not: numinput() fonksiyonu ile kullanıcıdan ekranda fload tipinde sayısal değer alınır. Bunu int ile integer türüne dönüştürülebiliriz
     textinput() fonksionu ile kullanıcıdan ekranda string tipinde veri alabiliriz.
"""

# import turtle
# print(turtle.position()) ## Ekrana bulunduğumuz poziyon koordinatlarını yazar (0.00,00.00)
# print(turtle.pos()) ## Ekrana bulunduğumuz poziyon koordinatlarını yazar (0.00,00.00)
# turtle.goto(100,100)
# print(turtle.pos())
# turtle.setposition(-50,-50)
# print(turtle.pos())
# turtle.setpos(0,0)
# print(turtle.pos())
# turtle.setposition(-50,-50)
# print(turtle.pos())
# turtle.reset()
# print(turtle.pos())
# turtle.setposition(78,32)
# print(turtle.pos())
# turtle.home()
# print(turtle.pos())

# turtle.setpos(0,100)
# turtle.goto(-200,200)
# turtle.setx(500)
# turtle.home()
# turtle.done() ## Grafik çizim ekranı kullanıcı X'den kapatan kadar açık kalmasını sağlar

# turtle.forward(100) # x ekseninde sağa doğru 100px ileri gitti
# turtle.right(90) #90 derece sağa dönüp 100px ilerledi
# turtle.fd(100) # x ekseninde sağa doğru 100px ileri gitti
# turtle.right(90) #90 derece sağa dönüp 100px ileri gitti
# turtle.backward(50) # x ekseninde sola doğru 50px geri gitti
# turtle.left(90) # 90 derece sola dönüp 50px ilerledi
# turtle.bk(50) # x ekseninde sola doğru 50px geri gitti
# turtle.done()


# from turtle import *
# #Kare çizimi
# fd(200)
# rt(90)
# fd(200)
# rt(90)
# fd(200)
# rt(90)
# fd(200)
# rt(90)
# done()

# import turtle
#print(turtle.getshapes()) # Ekrana ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle'] yazar

#Kaplumbağ ile kare çizimi
# turtle.shape('turtle')

# turtle.fd(200)
# turtle.rt(90)
# turtle.fd(200)
# turtle.rt(90)
# turtle.fd(200)
# turtle.rt(90)
# turtle.fd(200)
# turtle.rt(90)
# turtle.done()

#iç içe kare çizmek
# from turtle import *
# def kareCizim(mesafe):
#     for a in range(4):
#         forward(mesafe)
#         left(90)

# hideturtle()
# pensize(2)

# adet = int(input('Kaç Adet Kare İstiyorsunuz.: '))
# adet +=1
# for t in range(adet):
#     kareCizim(50*t)

# done()


# Üçgen Çizimi
# from turtle import *
# pensize(5)
# for t in range(3):
#     forward(200)
#     left(120) #Dönme işlemini dış açı ile gerçekleştirdiği için 120 derece değeri verildi. eğer right ile yapılsaydı ücçenin yönü aşağı doğru olurdu.

# Renkli üçgen çizimi
# from turtle import *
# pensize(5)
# color('red','yellow')

# def ucgen():
#     for t in range(3):
#         fd(200)
#         left(120)

# begin_fill()
# ucgen()
# end_fill()
# done()

