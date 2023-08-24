# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e irá sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-' * 40)
print(f'\033[1;30;47m{"GERADOR DE PALPITES":^40}\033[m')
print('-' * 40)
sleep(2)
n = int(input('Quantos palpites a serem criados? '))
palpite = []
sleep(2)
for c in range(0, n):
    for x in range(0, 6):
        numero = randint(1, 60)
        if numero in palpite:
            numero = randint(1, 60)
        palpite.append(numero)
        palpite.sort()
    print(f'Os palpites do jogo {c + 1}: {palpite[:]}')
    palpite.clear()
    sleep(1)
print('-'* 10, 'Boa Sorte', '-' * 10)