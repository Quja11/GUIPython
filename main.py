from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *

#Описание функций
def addCase():
    with open('data.txt', 'r+', encoding='utf-8') as file:
        file.seek(0, 2)
        case = input.get()
        print(len(case))
        if(len(case) > 3):
            messagebox.showinfo('Ежедневник', 'Запись успешно произведена')
            file.write(case + '\n')
            input.delete(0, END)

        else:
            messagebox.showerror('Ежедневник', 'Длина должна быть больше 3')

def viewCases():
    windowCases = Toplevel()
    windowCases.title('Список дел')
    windowCases.geometry('300x300')
    windowCases.configure(bg='orange')

    with open('data.txt', encoding='utf-8') as file:
        data = file.read()
        data = data.split('\n')

    #Убираем последний индекс (пустоту)
    data.pop(len(data)-1)
    print(data)

    amountCase = 0
    for i in range(len(data)):
        amountCase += 1
        label = Label(windowCases, text=str(i + 1) + ') ' + data[i], borderwidth=0, bg='orange', padx=5)
        label.place(x=5, y=(i+1)*30)

    checkBtn = Checkbutton(windowCases, text=i, variable=DISABLED, cursor='spider', bg='orange', offvalue='отключено')
    checkBtn.place(relx=0.7, y=(i+1)*30)

def changeConfig():

    def submitChange():
        with open('config.txt', 'w+t') as file:
            list_settings = (comboBoxColors.get(), comboBoxSizes.get())
            for i in range(len(list_settings)):
                file.write(list_settings[i] + '\n')

    windowConfig = Tk()
    windowConfig.title('Окно конфигурации')
    windowConfig.geometry('500x500+400+250')
    windowConfig.resizable(FALSE, FALSE)
    windowConfig.configure(bg='gray')

    label = Label(windowConfig, text='Введите новый цвет окна: ')
    label.place(x=20, y=20)

    label1 = Label(windowConfig, text='Введите новые размеры и координаты окна: ')
    label1.place(x=20, y=60)

    colorsMainWindow = ('red', 'green', 'orange', 'brown')
    comboBoxColors = ttk.Combobox(windowConfig, values=colorsMainWindow)
    comboBoxColors.current(0)
    comboBoxColors.place(relx=0.7, y=20)

    sizesMainWindow = ('500x500', '700x700')
    comboBoxSizes = ttk.Combobox(windowConfig, values=sizesMainWindow)
    comboBoxSizes.current(0)
    comboBoxSizes.place(relx=0.7, y=60)

    btnConfig = Button(windowConfig, text='Изменить конфигурацию', bg='black', fg='white', command=submitChange)
    btnConfig.place(x=150, y=100)



#Конфигурация программы
#Начальные значения

with open('config.txt') as file:
    list_settings = file.read().split('\n')

mainColor = list_settings[0]
sizesWindow = list_settings[1]

print(sizesWindow) 

#Инициализация главного окна приложения
window = Tk()

#Настройка окна приложения
window.title("Ежедневник")
window.iconbitmap(default='src/pic.ico')
window.geometry(sizesWindow  + '+' + str(400) + '+' + str(250))

window.configure(bg=mainColor)

#Позиционирование - ч/з метод place
#Создание надписей
label1 = Label(window, text='Введите дело: ', bg=mainColor)
label1.place(x=20, y=20)

#Дата и время
dateAndTime = datetime.now()
print(dateAndTime)
neededValesDateAndTime = str(dateAndTime.date()) + '\n' + str(dateAndTime.time().hour) + ':' + str(dateAndTime.time().minute) + ':' + str(dateAndTime.time().second)

labelDate = Label(window, text=neededValesDateAndTime, bg=mainColor)
labelDate.place(x=300, y=20)

#Добавление кнопок
btnAdd = Button(window, text='Записать', bg='black', fg='white', command=addCase)
btnAdd.place(x=20, y=60)

btnViewCases = Button(window, text='Просмотреть дела', bg='black', fg='white', command= viewCases)
btnViewCases.place(x=20, y=100)

btnConfig = Button(window, text='Изменить конфигурацию программы', bg='black', fg='white', command=changeConfig)
btnConfig.place(x=20, y=140)

#Добавление полей ввода
input = Entry(window)
input.place(x=120, y=20)
input.focus()

#Добавление progressBar
prBar = ttk.Progressbar(orient='horizontal', length=500, value=10, maximum=100)
prBar.start(1000)
prBar.place(x = 0, rely=0.5)



















window.mainloop()