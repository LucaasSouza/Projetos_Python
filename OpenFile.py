import os
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.frame = Frame(master, padx=10, pady=10)
        self.frame.pack()

        self.title = Label(self.frame, text='Insira o caminho do arquivo: ')
        self.title.pack(side=LEFT)

        self.input = Entry(self.frame, width=50)
        self.input.pack(side=RIGHT)

        self.frameBtn = Frame(master, pady=10)
        self.frameBtn.pack()

        self.button = Button(self.frameBtn, text="Abrir arquivo", command=self.loadFile)
        self.button.grid(row=0, column=1, padx=10)

        self.buttonCls = Button(self.frameBtn, text="Limpar texto", command=lambda: self.clsInput(True))
        self.buttonCls.grid(row=0, column=2, padx=10)

        self.frameMsg = Frame(master)
        self.frameMsg.pack()

        self.msg = Label(self.frameMsg, text="")
        self.msg.pack()

    def loadFile(self):
        if self.input.get() != '':
            try:
                os.startfile(self.input.get())
                if '.' in self.input.get(): print('Extensão do arquivo selecionado: ' + self.input.get().split('.')[-1])
                self.clsInput(False)
            except:
                self.frameMsg["pady"] = 5
                self.msg["text"] = "Arquivo não encontrado ou caminho inválido!"
        else:
            self.frameMsg["pady"] = 5
            self.msg["text"] = "Preencha o caminho do arquivo!"

    def clsInput(self, flag):
        self.frameMsg["pady"] = 0
        self.msg["text"] = ""

        if flag: self.input.delete(0, END)

root = Tk()
root.title("Abrir arquivo")
Application(root)
root.mainloop()