# Estou utilizando este compilador web, para evitar a fadiga: https://www.onlinegdb.com/online_python_compiler

import random

names = ('Hello', 'World', 'Hello world', 'Python', 'Javascript', 'HyperText Markup Language', 'Cascading Style Sheet', 'Structured Query Language', 'Hypertext Preprocessor', 'Java', 'Ruby', 'C', 'C sharp', 'C plus plus', 'Sintaxe', 'Functions', 'Methods')
message = names[random.randint(0, len(names) - 1)] # Mensagem que vai ser descoberta
placeHolder = '' # Faz o replace dos caracteres da string acima para '_'
tentativas = 6 # Quantidade de tentativas que o jogador vai ter

# Faz o replace dos caracteres da string acima para '_'
for m in message:
    placeHolder += '_' if m != ' ' else ' '

print(placeHolder)

# Loop do jogo
while tentativas > 0 and placeHolder != message:
    print('Digite uma letra: ')
    letter = input()
    errou = True # Flag que verifica se o caractere inserido pelo jogador foi correto
    
    for i in range(len(message)):
        if message[i] == letter: # Verifica se o caractere inserido pelo jogador foi correto
            errou = False
            placeHolder = placeHolder[:i] + letter + placeHolder[i + 1:]


    if letter == message:
        placeHolder = letter
        break
    elif errou: # Caso o caractere inserido pelo jogador seja errado 
        tentativas -= 1
        errou = True
        print(f'-- Você errou, faltam {tentativas} tentativas --')
        
    print(placeHolder)

if placeHolder == message:
    print('VOCÊ GANHOU!!!')
elif tentativas == 0:
    print(f'Você perdeu, a resposta era: {message}')
