# Importação das libs

import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Meu relógio')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background= '#1D1D1D')

def get_nome():
    nome_usuario = os.getlogin()
    nome.config(text=f'Olá, {nome_usuario}')

def get_data():
    data_atual = strftime('%a, %d/%m/%Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text=hora_atual)
    hora.after(1000, get_horas)

margin = tk.Canvas(root, width=600, height=60, bg='#1D1D1D', bd=0, highlightthickness=0, relief='ridge')
margin.pack()

nome = Label(root, bg='#1D1D1D', fg='#8e27ea', font=('Montserrat', 16))
nome.pack()

data = Label(root, bg='#1D1D1D', fg='#8e27ea', font=('Montserrat', 14))
data.pack(pady=2)

hora = Label(root, bg='#1D1D1D', fg='#8e27ea', font=('Montserrat', 64, 'bold'))
hora.pack(pady=2)


get_nome()
get_data()
get_horas()

root.mainloop()