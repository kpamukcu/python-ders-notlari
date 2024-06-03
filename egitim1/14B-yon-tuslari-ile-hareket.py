from turtle import *

shape('turtle')
pensize(4)
win = Screen()
win.setup(500,500) # px cinsinden ekran ölçüsü belirlendi

def solaDon():
    left(90)
    write('Sola Döndü')

def sagaDon():
    right(90)
    write('Sağa Döndü')

def ileri():
    forward(100)

def geri():
    backward(100)

win.onkeypress(solaDon,'Left')
win.onkeypress(sagaDon,'Right')
win.onkeypress(ileri,'Up')
win.onkeypress(geri,'Down')

win.listen() #Klavyden girilen tuşları dinleyip ona göre hareket edecek.
win.mainloop() #Kalvyeden sürekli giriş yapılabilmesini sağlar