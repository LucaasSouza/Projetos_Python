message = 'Hello World' # Mensagem que vai ser descoberta
placeHolder = '' # Faz o replace dos caracteres da string acima para '_'
tentativas = 6 # Quantidade de tentativas que o jogador vai ter

# Faz o replace dos caracteres da string acima para '_'
for m in message:
    placeHolder += '_' if m != ' ' else ' '

# Loop do jogo
while tentativas > 0 and placeHolder != message:
    print('Digite uma letra: ')
    letter = input()
    errou = True # Flag que verifica se o caractere inserido pelo jogador foi correto

    for i in range(len(message)):
        if message[i] == letter: # Verifica se o caractere inserido pelo jogador foi correto
            errou = False
            placeHolder = placeHolder[:i] + letter + placeHolder[i + 1:]
            print(placeHolder)

    # Caso o caractere inserido pelo jogador seja errado 
    if errou:
        tentativas -= 1
        errou = True
        print(f'-- Você errou, faltam {tentativas} tentativas --')

if placeHolder == message:
    print('VOCÊ GANHOU!!!')
elif tentativas == 0:
    print('-- Suas tentativas acabaram --')