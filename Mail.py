'''Данная программа предназначена для обработки текстовых файлов, выгружаемых из CRM Bitrix.\nОна приводит их к формату, допустимому при загрузке электронных адресов при организации маркетинговых рассылок.'''

import tkinter
from tkinter import *
root=Tk()
root.title("Обработчик текстовых файлов")
root.geometry("380x280")

Lb0=Label(root,text="Стандартная обработка",font=("Candara",14))
Lb0.place(x=100,y=8)

Lb1=Label(root,text="Данная программа предназначена для обработки \nфайлов с форматом *.txt",font=("Candara",9))
Lb1.place(x=50,y=45)

Lb2=Label(root,height=1,width=28,text='Загрузите файл',background="#fff",foreground="#A52A2A",relief="ridge",font=("Candara",9))
Lb2.place(x=190,y=90)

def func0():
    "Данная функция позволяет загрузить файл для работы."
    from tkinter import filedialog
    global File0
    File0=filedialog.askopenfilename()
    import os
    HeadFile0,TailFile0=os.path.split(File0)
    import sys
    sys.path.append(HeadFile0)
    Lb2=Label(root,height=1,width=28,text='Файл загружен',background="#fff",foreground="#458B00",relief="ridge",font=("Candara",9))
    Lb2.place(x=190,y=90)
    
def func1():
    "Данная функция убирает все запятые и переносит адреса на новую строку."
    try:
        File1=open(File0)
        File2=open('Tempfile.txt','w')
        for i in File1.readlines():
            L1=list(i)
            for l in L1:
                if l==',':
                    In=L1.index(l)
                    L1.pop(In)
                    L1.insert(In,'\n')
            I2=''.join(L1)
            print(I2)
            File2.write(I2)
        File2.close()
        File1.close()
        File1=open(File0,'w')
        File2=open('Tempfile.txt')
        for i in File2.readlines():
            print(i)
            File1.write(i)
        File2.close()
        File1.close()
        import os
        os.remove('Tempfile.txt')       
        Lb2=Label(root,height=1,width=28,text='Завершено',background="#fff",foreground="#458B00",relief="ridge",font=("Candara",9))
        Lb2.place(x=190,y=90)
    except NameError:
        func4()

def func2():
    "Данная функция убирает все пробелы."
    try:
        File1=open(File0)
        File2=open('Tempfile.txt','w')
        for i in File1.readlines():
            L1=list(i)
            for l in L1:
                if l==" ":
                    In=L1.index(l)
                    L1.pop(In)
            I2=''.join(L1)
            print(I2)
            File2.write(I2)
        File2.close()
        File1.close()
        File1=open(File0,'w')
        File2=open('Tempfile.txt')
        for i in File2.readlines():
            print(i)
            File1.write(i)
        File2.close()
        File1.close()
        import os
        os.remove('Tempfile.txt')
        Lb2=Label(root,height=1,width=28,text='Завершено',background="#fff",foreground="#458B00",relief="ridge",font=("Candara",9))
        Lb2.place(x=190,y=90)
    except NameError:
        func4()

def func3():
    "Данная функция убирает пустые строки."
    try:
        File1=open(File0)
        File2=open('Tempfile.txt','w')
        for i in File1.readlines():
            if len(i)<5:
                del(i)
            else:
                print(i)
                File2.write(i)
        File2.close()
        File1.close()
        File1=open(File0,'w')
        File2=open('Tempfile.txt')
        for i in File2.readlines():
            print(i)
            File1.write(i)
        File2.close()
        File1.close()
        import os
        os.remove('Tempfile.txt')
        Lb2=Label(root,height=1,width=28,text='Завершено',background="#fff",foreground="#458B00",relief="ridge",font=("Candara",9))
        Lb2.place(x=190,y=90)
    except NameError:
        func4()
    
def func4():
    "Данная функция выводит сообщение об ошибке,если не загружен файл для обработки."
    from tkinter.messagebox import showinfo
    showinfo(title="Системное сообщение",message="Пожалуйста,загрузите файл")
    
def func5():
    "Данная функция закрывает окно."
    root.destroy()
  
Btn0=Button(root,text="Обзор",font=("Candara",10),command=func0,width=20,height=1)
Btn0.place(x=20,y=90)

Btn1=Button(root,text="Убрать все запятые и перенести на новую строку",font=("Candara",10),command=func1,width=48,height=1)
Btn1.place(x=20,y=130)

Btn2=Button(root,text="Убрать все пробелы",font=("Candara",10),command=func2,width=48,height=1)
Btn2.place(x=20,y=160)

Btn3=Button(root,text="Убрать пустые строки",font=("Candara",10),command=func3,width=48,height=1)
Btn3.place(x=20,y=190)

Btn4=Button(root,text="Закрыть окно",font=("Candara",10),command=func5,width=48,height=1)
Btn4.place(x=20,y=230)

root.mainloop()

