import tkinter as tk
import random
from tkinter import messagebox

valorAleatorio = 0
valorMinimo = 1
valorMaximo = 100
valorAleatorio = random.randint(valorMinimo, valorMaximo)

def gerarNumeroAleatorio():
    nvalor = int(txt_valor.get())
    if nvalor > valorAleatorio:
        tk.Label(app, text = 'Valor alto, escolha um valor menor!', font = ('verdana', '9', 'bold'), foreground = '#000', anchor = 'center').place(x = 10, y = 220, width = 260)
    elif nvalor < valorAleatorio:
        tk.Label(app, text = 'Valor baixo, escolha um valor maior', font = ('verdana', '9', 'bold'), foreground = '#000', anchor = 'center').place(x = 10, y = 220, width = 260)
    elif nvalor == valorAleatorio:
        tk.caixa = messagebox.showinfo('Informação', 'Parabéns, você conseguiu acertar!')
        app.quit()
    #print(valorAleatorio)

app = tk.Tk()
app.title('Acerte o número')
app.geometry('280x300+600+150')
app.configure(bg = 'blue')

tk.Label(app, text = 'Adivinhe o número sortado', font = ('verdana', '12', 'italic', 'bold'), foreground = '#000', anchor = 'center').place(x = 10, y = 30, width = 260)
tk.Label(app, text = 'Digite um número inteiro entre 1 e 100', font = ('verdana', '8', 'bold'), foreground = '#000', anchor = 'center').place(x = 10, y = 70, width = 260)
txt_valor = tk.Entry(app, font = ('verdana', '11', 'bold'))
txt_valor.place(x = 110, y = 110, width = 50, height = 20)

tk.Button(app, text = 'SORTEAR', command = gerarNumeroAleatorio).place(x = 85, y = 160, width = 100, height = 30)


app.mainloop()