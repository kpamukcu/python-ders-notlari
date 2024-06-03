from turtle import *
pensize(3)
win = Screen()

win.setup(200,200)

def nokta(x,y):
    goto(x,y)

win.onclick(nokta) #Mouse tıklandığında nokta fonksiyonu çalışacak

mainloop() #veya done ile turtle pencerei sabitlendi