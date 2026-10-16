from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk

#Упражнение 1
# root = Tk()
# root.title("Калькулятор")
# root.geometry("500x500")
#
# def calc(*args):
#     value = str(strok.get())
#     res.set(eval(value))
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# strok = StringVar()
# strok_entry = ttk.Entry(mainframe, width=20, textvariable=strok)
# strok_entry.grid(column=1, row=0, sticky=(N, W, E, S))
#
# res = StringVar()
# ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))
#
#
# btn = ttk.Button(mainframe, text="calc", command=calc).grid(column=3, row=3)
# root.bind("<Return>", calc)
# strok_entry.focus()
# root.mainloop()

#Упражнение 2

# root = Tk()
# root.title("Калькулятор ИМТ")
# root.geometry("400x400")
#
# def calc(*args):
#     h = float(he.get())
#     m = float(we.get())
#     res.set(f"{m/h**2:.1f}")
#
#
# he = ttk.Entry(root, width=10)
# he.grid(column=0, row=0, padx=10, pady=10)
# we = ttk.Entry(root, width=10)
# we.grid(column=0, row=1, padx=10)
# ttk.Label(root, text="Рост(Вводите в виде: 1.81)").grid(row=0, column=1, sticky='e')
# ttk.Label(root, text="Масса(Вводите в виде: 78.3)").grid(row=1, column=1, sticky='e')
#
# res = StringVar()
# ttk.Label(root, textvariable=res).grid(column=2, row=2, sticky=(W, E))
#
#
# btn = ttk.Button(root, text="Получить значение", command=calc).grid(column=4, row=4)

# root.bind("<Return>", calc)
# root.mainloop()


#Упражнение 3

# import pandas as pd
#
# films = pd.read_csv('imdb_top_250.csv')
# genres = list(films['Genre'])
# films = list(films["Title"])
#
# root = Tk()
# root.geometry('500x500')
# root.title("Генератор фильмов")
#
# def f(*args):
#     g = str(fil.get())
#     k=0
#     w=""
#     if g in genres:
#         for i in range(10000000):
#             a=np.random.randint(len(films))
#             w = films[a]
#             if g in genres[a]:
#                 break
#     if len(w)!=0:
#         res.set(w)
#     else:
#         res.set("Нет такого жанра")
# fil = ttk.Entry(root, width=40)
# fil.grid(row=0, column=1)
# ttk.Label(root, text = "Введите жанр ").grid(row=0, column=2)
# res = StringVar()
# ttk.Label(root, textvariable=res).grid(column=2, row=2, sticky=(W, E))
# btn = ttk.Button(root, text="Получить фильм", command=f).grid(column=4, row=4)
#
# root.bind("<Return>", f)
# root.mainloop()

#Упражнение 4

# root = Tk()
# root.title("Подбор цветов")
# col = ttk.Entry(root, width=30)
# col.pack()
#
# def f(*args):
#     a = str(col.get())
#     x1 = a[1:3]
#     x2 = a[3:5]
#     x3 = a[5:7]
#     x1 =int(x1, 16)
#     x2 =int(x2, 16)
#     x3 =int(x3, 16)
#     x1 = 255 - x1
#     x2 = 255 - x2
#     x3 = 255 - x3
#     x1 = hex(x1)[2:]
#     x2 = hex(x2)[2:]
#     x3 = hex(x3)[2:]
#     if len(x1)==1:
#         x1 = '0'+x1
#     if len(x2)==1:
#         x2 = '0'+x2
#     if len(x3)==1:
#         x3 = '0'+x3
#     x ="#" + x1 + x2 + x3
#     canvas.delete("all")
#     canvas.create_rectangle(100, 100,300,300, fill = a, outline = "black")
#     canvas.create_rectangle(400, 100, 600, 300, fill=x)
#     canvas.update()
#
# btn = ttk.Button(root, text="Получить цвет", command=f)
# btn.pack()
# a =ttk.Label(root, text = "Старый цвет                                                  Новый цвет")
# a.pack()
# canvas = Canvas(root, width=700, height=700)
# canvas.pack()
# root.bind("<Return>", f)
# root.mainloop()


#Упражнение 5
# from random import randint
#
# WIDTH = 500
# HEIGHT = 500
# colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "orange"]
#
# class Ball:
#     def __init__(self):
#         self.R = randint(10, 50) #храним размер, при каждом создании объекта будет выбираться случайно
#         self.x = randint(self.R, root.winfo_width() - self.R) # храним положение по x и y
#         self.y = randint(self.R, root.winfo_height() - self.R)
#         self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
#         self.ball_id = canvas.create_oval(self.x - self.R,
#                                      self.y - self.R,
#                                      self.x + self.R,
#                                      self.y + self.R, fill=colors[randint(0,len(colors)-1)]) # при создании шарика отрисовываем его
#
#     def move(self):
#         self.x += self.dx
#         self.y += self.dy
#         if self.x + self.R > root.winfo_width() or self.x - self.R <= 0: # отражение от стенок
#             self.dx = -self.dx
#         if self.y + self.R > root.winfo_height() or self.y - self.R <= 0: # отр
#             self.dy = -self.dy
#
#     def show(self):
#         canvas.move(self.ball_id, self.dx, self.dy)
#
#
#
# #здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
# def tick():
#     for ball in balls:
#         ball.move()
#         ball.show()
#     root.after(50, tick)
#
# def click_handler(event):
#     balls.append(Ball())
#
# root = Tk()
# root.geometry(f'500x500')
# root.update()
# canvas = Canvas(root)
#
# canvas.pack(fill = BOTH, expand = True)
# #сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
# canvas.bind('<Button-1>', click_handler)
# balls = [Ball() for i in range(5)]
# # делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
# tick()
# root.mainloop()


#Упражнение 6
import pandas as pd
root = Tk()
root.geometry("500x500")
root.title("График для лабы")
a = ttk.Label(root, text = "Введите полное имя файла + .csv")
a.pack()
name = ttk.Entry(root, width=30)
name.pack()
b = ttk.Label(root, text = "Введите полное имя файла куда хотите сохранить")
b.pack()
nam = ttk.Entry(root, width=30)
nam.pack()
def f(*args):
    q = str(name.get())
    w = str(nam.get())
    file = pd.read_csv(q)
    x = np.array(list(file["X"]))
    y = np.array(list(file["Y"]))

    def mnk(x, y):
        n = len(x)
        b = (n*np.sum(x*y) - np.sum(x) * np.sum(y)) / (n * np.sum(x*x)  -(np.sum(x))**2)
        a = (np.sum(y) - b*np.sum(x))/ n
        return a, b
    a,b = mnk(x,y)
    x1 = np.linspace(min(x), max(x), 100)
    y1 = np.linspace(min(y), max(y), 100)
    y1 = y1*b +a
    plt.plot(x,y,"x")
    plt.plot(x1,y1, color = "r")
    plt.savefig(f"{w+".jpg"}")
    res.set(f"Коэффициенты: k = {a}, b = {b} , Название файла: {w+".jpg"}")

btn = ttk.Button(root, text="Получить график", command=f)
btn.pack()
root.bind("<Return>", f)
res = StringVar()
r =  ttk.Label(root, textvariable=res)
r.pack()
root.mainloop()
