#importando tkinter
from tkinter import *
from tkinter import ttk 

#cores
preta = "#21130d"

janela=Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=preta)

Frame_tela = Frame(janela, width=235, height=50)
Frame_tela.grid(row=0, column=0,)

Frame_corpo = Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1, column=0)


janela.mainloop()
