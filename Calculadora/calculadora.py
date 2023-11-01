from tkinter import *
from tkinter import messagebox

class Application:
    def __init__(self, master = None):
        self.frame = Frame(master, padx=10, pady=5)
        self.frame.pack()

        self.label = Label(self.frame, text='Digite o primeiro número:')
        self.label.grid(row=1, column=1)

        self.input = Entry(self.frame)
        self.input.grid(row=1, column=2)

        self.label2 = Label(self.frame, text='Digite o segundo número:')
        self.label2.grid(row=2, column=1)

        self.input2 = Entry(self.frame)
        self.input2.grid(row=2, column=2)

        self.btnSom = Button(self.frame, text='+', command=lambda: self.calc('+'), width=5)
        self.btnSom.grid(row=1, column=3, padx=8, pady=4)

        self.btnSub = Button(self.frame, text='-', command=lambda: self.calc('-'), width=5)
        self.btnSub.grid(row=1, column=4, padx=8, pady=4)

        self.btnMul = Button(self.frame, text='*', command=lambda: self.calc('*'), width=5)
        self.btnMul.grid(row=2, column=3, padx=8, pady=4)

        self.btnDiv = Button(self.frame, text='/', command=lambda: self.calc('/'), width=5)
        self.btnDiv.grid(row=2, column=4, padx=8, pady=4)

        self.btnClose = Button(self.frame, text='Limpar', command=self.clear)
        self.btnClose.grid(row=4, column=4)

        self.result = Label(self.frame)

    def calc(self, ope):
        inp1 = self.input #Instância dos dois inputs
        inp2 = self.input2

        def showMessage(result): #Adiciona a mensagem ao label oculto
            self.result['text'] = f'O resultado é: {result}'
            self.result.grid(sticky='W', row=4, column=1)

        try:
            fixNumber = lambda num: float(num.replace(',', '.')) #Retorna o parâmetro trocando ',' por '.', e seu valor no tipo float

            num1 = fixNumber(inp1.get()) #Armazena o valor dos dois inputs com a formatação da função acima
            num2 = fixNumber(inp2.get())

            if ope == '+':
                showMessage(round(num1 + num2, 2))
            elif ope == '-':
                showMessage(round(num1 - num2, 2))
            elif ope == '*':
                showMessage(round(num1 * num2, 2))
            elif ope == '/':
                showMessage(round(num1 / num2, 2))
        except: #Caso dê algum erro, é retornado as informações abaixo
            messagebox.showerror(title='ERRO', message='Não foi possível executar a operação')
            self.clear()

    def clear(self): #Função chamada no botão "Limpar"
        inp1 = self.input

        self.result.grid_remove()
        inp1.delete(0, END) #Limpa os números que estavam nos inputs
        self.input2.delete(0, END)
        inp1.focus() #Dá foco no primeiro input

root = Tk()
root.title('Calculadora')
root.resizable(False, False)
Application(root)
root.mainloop()