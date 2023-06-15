from tkinter import *

dados = ['hello', 'world', 'ola', 'mundo']
class Application:
    def __init__(self, master=None):
        self.frameTitle = Frame(master)
        self.frameTitle.pack()

        self.title = Label(self.frameTitle, text="Login")
        self.title.pack()

        self.frame = Frame(master)
        self.frame["padx"] = 5
        self.frame["pady"] = 5
        self.frame.pack()

        self.user = Label(self.frame, text="Usuário: ")
        self.user.pack(side=LEFT)

        self.inputUser = Entry(self.frame)
        self.inputUser.pack(side=RIGHT)

        self.frame1 = Frame(master)
        self.frame1["padx"] = 5
        self.frame1["pady"] = 5
        self.frame1.pack()

        self.password = Label(self.frame1, text="Senha: ")
        self.password.pack(side=LEFT)

        self.inputPassword = Entry(self.frame1, show="*")
        self.inputPassword.pack(side=RIGHT)

        self.frameButton = Frame(master)
        self.frameButton["padx"] = 5
        self.frameButton["pady"] = 5
        self.frameButton.pack()

        self.button = Button(self.frameButton, text="Entrar", command=self.Login)
        self.button.pack(side=LEFT)

        self.buttonQuit = Button(self.frameButton, text="Sair", command=self.frame.quit)
        self.buttonQuit.pack(side=RIGHT)

        self.frameRes = Frame(master)
        self.frameRes.pack()

        self.text = Label(self.frameRes, text="")
        self.text.pack()

    def Login(self):
        if (self.inputUser.get() == 'admin') and (self.inputPassword.get() == '12345'):
            self.text["text"] = f'Bem vindo {self.inputUser.get()}'
        else:
            self.text["text"] = 'Erro na autenticação'

root = Tk()
Application(root)
root.mainloop()