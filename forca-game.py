message = 'Hello World'
placeHolder = ''
tentativas = 6

for m in message:
    placeHolder += '_' if m != ' ' else ' '

while tentativas > 0 and placeHolder != message:
    print('Digite uma letra: ')
    letter = input()
    errou = True

    for i in range(len(message)):
        if message[i] == letter:
            errou = False
            placeHolder = placeHolder[:i] + letter + placeHolder[i + 1:]
            print(placeHolder)

    if errou:
        tentativas -= 1
        errou = True
        print(f'-- Você errou, faltam {tentativas} tentativas --')

if placeHolder == message:
    print('VOCÊ GANHOU!!!')
elif tentativas == 0:
    print('-- Suas tentativas acabaram --')