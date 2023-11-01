import qrcode
from tkinter import *
from PIL import ImageTk

class Application:
    def __init__(self, master=None):
        self.topFrame = Frame(master, padx=8, pady=4)
        self.topFrame.pack()

        self.label = Label(self.topFrame, text='Insira a mensagem que deseja gerar o QRCode:')
        self.label.grid(row=1, column=1)

        self.input = Entry(self.topFrame, width=70)
        self.input.grid(row=1, column=2)
        self.input.focus()

        self.bottomFrame = Frame(master, pady=8)
        self.bottomFrame.pack()

        self.generateBtn = Button(self.bottomFrame, text='Gerar QRCode', width=30, command=self.generateQRCode)
        self.generateBtn.grid(row=2, column=1, padx=12)

        self.deleteBtn = Button(self.bottomFrame, text='Limpar dados', width=30, command=lambda: self.input.delete(0, END))
        self.deleteBtn.grid(row=2, column=2)

        self.imagem = Label(master, text="Gerando QR Code")

    def generateQRCode(self):
        try:
            text = self.input.get()

            if(len(text) > 0):
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                qr.add_data(text)
                qr.make(fit=True)
                finalQr = qr.make_image(fill_color="black", back_color="white")

                photo = ImageTk.PhotoImage(finalQr)
                self.imagem['image'] = photo
                self.imagem.image = photo
                self.imagem.pack(pady=4)
            else:
                self.imagem['text'] = 'Digite alguma coisa'
                self.imagem.pack(pady=4)
        except NameError:
            print(NameError)

root = Tk()
root.title('Gerador de QRCode 2.0')
root.resizable(False, False)
Application(root)
root.mainloop()