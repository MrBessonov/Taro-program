import random
from PIL import Image, ImageTk
from tkinter import Tk, Menu, Button, END, Text, LEFT, Frame, CENTER, NW, RAISED
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile


def divination():
    with open("tarot.txt", "r", encoding="utf-8") as f: cards = [line.strip() for line in f]
    fortune = cards[random.randint(0, len(cards))]
    i = fortune.find(".")
    return f'Ваша карта: {fortune[:i+1]}\nЕё значение: {fortune[i+2:]}'


def show_divination():
    text_of_divination.configure(state='normal')  # enable insert
    text_of_divination.insert(END, divination() + '\n')
    text_of_divination.configure()  # disable editing


def save():
    file = asksaveasfile()
    file_text = str(text_of_divination.get(1.0, END))
    file.write(file_text)
    file.close()


def clear():
    text_of_divination.delete(1.0, END)


def quit():
    window.destroy()


def about():
    showinfo("О программе.", "Простой симулятор гадания на картах Таро. Выдаёт один простой расклад без интерпретации.")


def rules():
    showinfo("Правила.", "Задумайте вопрос. Поочередно нажмите на каждую карту. Ответ складывается из пяти частей:\n"
                         "1) тема вопроса, цель или желание;\n"
                         "2) прошлое, которое привело к текущей ситуации;\n"
                         "3) вероятное развитие текущей ситуации;\n"
                         "4) препятствия и трудности, которые предстоит преодолеть;\n"
                         "5) совет, как преодолеть препятствия.")

window = Tk()
window.geometry("885x485")
window.title("Таро")
window.config(background="black")

icon = ImageTk.PhotoImage(Image.open("icon.png"))
window.iconphoto(True, icon)

cover = ImageTk.PhotoImage(Image.open("cover.png"))

frame = Frame(window, bg="black")
frame.place(anchor=NW)

theme_of_question = Button(frame, text="Тема\nвопроса\n\n\n\n\n\n", fg="white", font=("Arial", 20),
                           width=150, image=cover, compound=CENTER, command=show_divination)
theme_of_question.pack(side=LEFT)
past = Button(frame, text="Прошлое\n\n\n\n\n\n", font=("Comic sans", 20), fg="white", width=150,
              image=cover, compound=CENTER, command=show_divination)
past.pack(side=LEFT)
possibility = Button(frame, text="Вероятное\nбудущее\n\n\n\n\n\n", fg="white", font=("Times New Roman", 20),
                     width=150, image=cover, compound=CENTER, command=show_divination)
possibility.pack(side=LEFT)
difficulties = Button(frame, text="Сложности\n\n\n\n\n\n", font=("Arial", 20), fg="white",
                      width=150, image=cover, compound=CENTER, command=show_divination)
difficulties.pack(side=LEFT)
advice = Button(frame, text="Совет\n\n\n\n\n\n", font=("Arial", 20), width=150, fg="white",
                image=cover, compound=CENTER, command=show_divination)
advice.pack(side=LEFT)

new = Button(window, text="Новый\nрасклад", font=("Arial", 10), width=10, fg="black", relief=RAISED,
             bd=5, command=clear)
new.place(x=790, y=0)
save = Button(window, text="Сохранить\nрасклад", font=("Arial", 10), width=10, fg="black", relief=RAISED,
              bd=5, command=save)
save.place(x=790, y=50)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Расклад", menu=file_menu)
file_menu.add_command(label="Новый расклад", command=clear)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Помощь", menu=help_menu)
help_menu.add_command(label="Правила", command=rules)
help_menu.add_command(label="О программе", command=about)


text_of_divination = Text(window, font=("Comic sans", 13), bg="black", fg="white", width=500)
text_of_divination.place(x=0, y=280)

window.mainloop()
