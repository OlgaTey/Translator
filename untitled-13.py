'''import json 
with open('personal.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 
    text = str(text)'''
from tkinter import *

def work():
    question = 'Покажи все записи'
    text = t.get('1.0', END)
    main_place = 'from sport s'
    place = '*'
    if 'вид' in question:
        place = 'section'
    elif 'мероприят' in question:
        place = 'section'
    elif 'подсекц' in question:
        place = 'subsection'
    elif 'соревнован' in question:
        place = 'title'
    if 'начал' in question:
        time = 'start'
    if 'вс' in question:
        a = 'select ' + place + ' ' + main_place
    if 'сколько' in question or 'Сколько' in question or 'количеств' in question:
        a = 'select ' +  'count(' + place + ') ' + main_place
    if 'Как' in question:
        a = 'select ' +  'distinct ' + place + ' ' + main_place
    t1.delete('1.0', END)
    t1.insert('1.0', a)

root = Tk()
root.geometry('500x350')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = 'black'

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите запрос на естественном языке')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Перевести', command=work)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()