from tkinter import *
import requests

root = Tk()
root.title('Отслеживание погоды')
root['bg'] = '#fafafa'
root.geometry('300x300')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300,width=300)
canvas.pack()

frame = Frame(root, bg = '#fff200', bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight= 0.7)

title = Label(frame, text="текст надписи", bg='lightblue', font=40)
title.pack()

btn = Button(frame, text='Это кнопка', bg='pink')
btn.pack()

btn_click = btn.click

def btn_click():
    print('Кнопка нажата!')

frame = Frame(root, bg='#ffb700', bd=5)
btn = Button(frame, text='Это кнопка', bg='pink', command= btn_click)

loginInput = Entry(frame, bg='white', font= 30)
loginInput.pack()
passField = Entry(frame, bg='white', show='*')
passField.pack()
def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные{str(login)}, {str(password)}'
    messagebox.showinfo(title='Окно с данными', message=info_str)
def get_weather():
    city = cityField.get()
    key = 'gdgs'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}

    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}:{weather["main"]["temp"]}'

root.mainloop()
