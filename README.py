#importando tkinter
from tkinter import *
from tkinter import ttk 

#cores
Preta = "#21130d"
Branca = "#e6f2e9"
Azul = "#3b4c96" 
Cinza = "#888d8f"
Laranja = "#f7a848"

janela=Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=Preta)

#Crianodo frames
Frame_tela = Frame(janela, width=235, height=50, bg=Azul)
Frame_tela.grid(row=0, column=0,)

Frame_corpo = Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1, column=0)

 #Variavel todos os valores
Todos_valores = ''


#Criando Função

def Entrada_valores(event):

    global Todos_valores 
    
    Todos_valores = Todos_valores + str(event)

    #Passando valores na tela 

    Valor_texto.set(Todos_valores)

# Calculos 

def calcular ():

    global Todos_valores
    resultado = eval(Todos_valores)
    Valor_texto.set(str(resultado))   


#Limpar tela

def limpar_tela():

    global Todos_valores
    Todos_valores = ""
    Valor_texto.set("")
     


#Criando Lable (Tela)

Valor_texto = StringVar() 

Tela_Label = Label(Frame_tela, textvariable=Valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 17 bold'), bg=Azul, fg=Branca)
Tela_Label.place(x=0, y=0)

#Criando botões
B1 = Button(Frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B1.place(x=0, y=0)
B2 = Button(Frame_corpo, command = lambda: Entrada_valores('%'), text="%", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B2.place(x=120, y=0)
B3 = Button(Frame_corpo, command = lambda: Entrada_valores('/'), text="/", width=5, height=2, bg=Laranja, fg=Branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B3.place(x=180, y=0)

B4 = Button(Frame_corpo, command = lambda: Entrada_valores('7'), text="7", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B4.place(x=0, y=52)
B5 = Button(Frame_corpo, command = lambda: Entrada_valores('8'), text="8", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B5.place(x=60, y=52)
B6 = Button(Frame_corpo, command = lambda: Entrada_valores('9'), text="9", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B6.place(x=120, y=52)
B7 = Button(Frame_corpo, command = lambda: Entrada_valores('*'), text="*", width=5, height=2, bg=Laranja, fg=Branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B7.place(x=180, y=52)

B8 = Button(Frame_corpo, command = lambda: Entrada_valores('4'), text="4", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B8.place(x=0, y=104)
B9 = Button(Frame_corpo, command = lambda: Entrada_valores('5'), text="5", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B9.place(x=60, y=104)
B10 = Button(Frame_corpo, command = lambda: Entrada_valores('6'), text="6", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B10.place(x=120, y=104)
B11 = Button(Frame_corpo, command = lambda: Entrada_valores('-'), text="-", width=5, height=2, bg=Laranja, fg=Branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B11.place(x=180, y=104)

B12 = Button(Frame_corpo, command = lambda: Entrada_valores('1'), text="1", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B12.place(x=0, y=156)
B13 = Button(Frame_corpo, command = lambda: Entrada_valores('2'), text="2", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B13.place(x=60, y=156)
B14 = Button(Frame_corpo, command = lambda: Entrada_valores('3'), text="3", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B14.place(x=120, y=156)
B15 = Button(Frame_corpo, command = lambda: Entrada_valores('+'), text="+", width=5, height=2, bg=Laranja, fg=Branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B15.place(x=180, y=156)

B16 = Button(Frame_corpo, command = lambda: Entrada_valores('0'), text="0", width=11, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B16.place(x=0, y=208)
B17 = Button(Frame_corpo, command = lambda: Entrada_valores('.'), text=".", width=5, height=2, bg=Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B17.place(x=120, y=208)
B18 = Button(Frame_corpo, command = calcular, text="=", width=5, height=2, bg=Laranja, fg=Branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B18.place(x=180, y=208)


janela.mainloop()
