import tkinter as tk
import requests
from threading import Thread

api = 'http://api.quotable.io/random'
quotes = []
quote_number = 0

okno = tk.Tk()
okno.geometry('900x260')
okno.title('Цитатник')
okno.grid_columnconfigure(0, weight=1)
okno.resizable(False, False)
okno.configure(bg="grey")

def preload_quotes():
    global quotes

    print("***Грузим еще цитаты***")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "От " + author
        print(content)

        quotes.append(quote)

    print('***Мы закончили***')

preload_quotes()

def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()  #как только значение ячейки массива совпадет со значением третьей с конца ячейки массива, запустится загрузка цитат



quote_label = tk.Label(okno, text="Нажмите на кнопочку, чтобы сгенерировать рандомный номер",
                         height=6,
                         pady=10,
                         wraplength=800,
                         font=("Helvetica", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Сгенерировать", command=get_random_quote, bg='#0052cc', fg='#ffffff',
                   activebackground='grey', font=("Helvetica", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)
if __name__ == "__main__":
    okno.mainloop()

import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=453c4fb46fdb67359e75f049a3f8e50e"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Минимальная температура: " + str(min_temp) + "°C" + "\n" + "Максимальная температура: " + str(
        max_temp) + "°C" + "\n" + "Давление: " + str(pressure) + "\n" + "Влажность: " + str(
        humidity) + "\n" + "Скорость ветра: " + str(wind) + "\n" + "Восход: " + sunrise + "\n" + "Закат: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk() #Дизайн виджета
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()

