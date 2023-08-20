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
frame1_style = ttk.Style()
frame1_style.configure("frame1.TFrame", background='#E9967A')

frame2_style = ttk.Style()
frame2_style.configure("frame2.TFrame", background='#B0E0E6')

frame2_labels_style = ttk.Style()
frame2_labels_style.configure("My.TLabel", background='#B0E0E6', foreground='black', relief='groove', padding=0)



#1 frame (рамка)
frame1 = ttk.Frame(window, borderwidth=2, height=500, width=250, padding=10, style="frame1.TFrame")

labelInput = Label(frame1, text='Введите дело: ', borderwidth=2, relief='ridge')
labelInput.place(x=0, y=0)

input = Entry(frame1, cursor='pirate')
input.place(x=100, y=0)
input.focus()

btnAdd = Button(frame1, text='Записать', bg='black', fg='white', command=addCase)
btnAdd.place(x=0, y=30)

frame1.place(x=0, y=0)

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

























#Отображение дел в GUI
with open('data.txt', 'r+', encoding='utf-8') as file:
    cases = []
    for i in file:
        cases.append(i)
    

#2 рамка (каркас)
frame2 = ttk.Frame(window, borderwidth=2, height=500, width=250, style="frame2.TFrame")

labelCases = ttk.Label(frame2, text='Список: ', style="My.TLabel")
labelCases.place(x=95, y=0)

lengthOfListCases = len(cases)
index = lengthOfListCases - lengthOfListCases + 1

for i in cases:
    ttk.Label(frame2, text=f'{index}) {i}', style="My.TLabel").place(x=10, y=index*35)
    index += 1

frame2.place(x=250, y=0)















window.config(menu=main_menu, bg=mainColor)
window.mainloop()