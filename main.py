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

def aboutOfDev():
    messagebox.showinfo('Информация о разработчике', 'Разработчик: Тахаев А.Г.\nПочта: takhaev80@bk.ru')


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
window.title('Ежедневник')
window.iconbitmap(default='src/pic.ico')
window.geometry(sizesWindow  + '+' + str(400) + '+' + str(250))

#Глобальное отключение всех пунктир.линий в меню
window.option_add("*tearOff", FALSE)

#Настройка стилей ч/з объект Style модуля ttk
frame_style = ttk.Style()
frame_style.configure(".TFrame",
                    background='#E9967A')



#1 frame (рамка)
frame = ttk.Frame(window, borderwidth=2, relief=GROOVE, height=80, width=500, padding=10, style=".TFrame")

labelInput = Label(frame, text='Введите дело: ', borderwidth=2, relief='ridge')
labelInput.place(x=0, y=0)

input = Entry(frame, cursor='pirate')
input.place(x=150, y=0)
input.focus()

dateAndTime = datetime.now()
neededValesDateAndTime = str(dateAndTime.date()) + '\n' + str(dateAndTime.time().hour) + ':' + str(dateAndTime.time().minute) + ':' + str(dateAndTime.time().second)
labelDate = Label(frame, text=neededValesDateAndTime)
labelDate.place(x=350, y=0)

btnAdd = Button(frame, text='Записать', bg='black', fg='white', command=addCase)
btnAdd.place(x=0, y=30)

frame.place(x=0, y=0)


btnViewCases = Button(window, text='Просмотреть дела', bg='black', fg='white')
btnViewCases.place(x=20, y=100)

btnConfig = Button(window, text='Изменить конфигурацию программы', bg='black', fg='white', command=changeConfig)
btnConfig.place(x=20, y=140)

#Добавление progressBar
#prBar = ttk.Progressbar(orient='horizontal', length=500, value=10, maximum=100)
#prBar.start(1000)
#prBar.place(x = 0, rely=0.5)

#Добавление фрейма (рамки, каркаса)
#frame = ttk.Frame(window, borderwidth=1, relief=SOLID, height=500, width=500, padding=10)
#but = Button(frame, text='Пример')
#but.place(x=0, y=0)
#but1 = Button(frame, text='Пример')
#but1.place(x=0, y=80)
#frame.place(x=0, y=180)

#Cоздание меню
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=lambda: window.destroy())

settings_menu = Menu()

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Настройки', menu=settings_menu)
main_menu.add_command(label="Инфо", command=aboutOfDev)












window.config(menu=main_menu, bg=mainColor)
window.mainloop()