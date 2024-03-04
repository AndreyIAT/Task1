from tkinter import *
import pymorphy2
from collections import Counter
import pyperclip

def set_text():
    # получаем текст из первого поля
    edittext = text1.get(1.0, END)
    text_ob = remove_text(edittext)
    # разбиваем текст на список слов
    texts = text_ob.split()
    # нормализация слов
    for elem in texts:
        elem = norm(elem)
    # выводим самое частое слово
    collect = Counter(texts).most_common(1)
    text2.insert('end', collect[0])
    text2.insert('end', '\n')
    # выводим самое редкое слово
    collect2 = Counter(texts).most_common()
    text2.insert('end', collect2[len(collect2) - 1])


def remove_text(text_x):
    text_x = text_x.replace(',', '')
    text_x = text_x.replace('.', '')
    text_x = text_x.replace(':', '')
    text_x = text_x.replace(';', '')
    text_x = text_x.replace('?', '')
    text_x = text_x.replace('!', '')
    return text_x


def norm(x):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(x)[0]
    return p.normal_form


def buffer_text():
    text1.insert('end', pyperclip.paste())


# Инициализация и настройка окна программы
root = Tk()
root.title("Лабораторная работа 1")
root.geometry("500x550")
root.resizable(False, False)

label1 = Label(text="Вставьте текст в первое поле")
label1.pack()

text1 = Text(height=8, wrap="word")
text1.pack(anchor=N, fill=X)

btn = Button(text="Обработать текст", command=set_text)
btn.pack()

btn = Button(text="Вставить текст из буфера обмена", command=buffer_text)
btn.pack()

text2 = Text(height=8, wrap="word")
text2.pack(anchor=S, fill=X)

# Запуск программы
root.mainloop()