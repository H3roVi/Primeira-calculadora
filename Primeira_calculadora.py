from tkinter import *
from tkinter import ttk

cor1 = "#000000"  #preto
cor2 = "#FFFFFF"  #white
cor3 = "#5754F7"  #azul
cor4 = "#4C4B4C"  #cizento
cor5 = "#F88E03"  #laranja

janela =Tk()
janela.title("calculadora")
janela.geometry("321x411")

#Janela A e B
frame_tela = Frame(janela, width=350, height=90, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=420,)
frame_corpo.grid(row=1, column=0)

# variavel todos valores
todos_valores = ''

#criando Label
valor_texto = StringVar()

#criando função
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando valor para tela
    valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

    todos_valores = ""

#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")

app_label = Label(frame_tela, textvariable=valor_texto, width=17 , height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 22 bold'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)

#Botões
b_1 = Button(frame_corpo, command = limpar_tela, text="C", width=15, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=160, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=241, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=70)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=70)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=70)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=241, y=70)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=241, y=130)
b_4 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=130)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=130)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=130)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=241, y=190)
b_4 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=190)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=190)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=190)

b_1 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=15, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=250)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=7, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=250)
b_7 = Button(frame_corpo, command = calcular, text="=", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=241, y=250)


janela.mainloop()