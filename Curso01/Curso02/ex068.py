# Crie um programa que jogue par ou impar com o usuario. O jogo só sera encerrado quando o usuario perder, mostrando
# o total de vitórias consecutivas que ele conquistou no fim do jogo.

from random import randint
cont = 0
while True:
    print('-=-=-=-= \033[1;31;40mPAR OU IMPAR\033[m =-=-=-=-')
    pc = randint(1, 5)
    user = str(input('Par ou ímpar: ')).strip().upper()[0]
    n = int(input('Jogador: '))
    print(f'PC: {pc}')
    r = (n + pc) % 2
    if r == 0:
        if user == 'P':
            print(f'{pc + n} é PAR. \033[1;32mVocê ganhou\033[m.')
            cont += 1
        if user == 'I':
            print(f'{pc + n} é PAR. Você \033[1;31mperdeu\033[m')
            break
    else:
        if user == 'I':
            print(f'{pc + n} é ÍMPAR. Você \033[1;32mganhou\033[m.')
            cont += 1
        if user == 'P':
            print(f'{pc + n} é ÍMPAR. Você \033[1;31mperdeu\033[m')
            break

print(f'Você ganhou {cont} vezes seguidas.')
