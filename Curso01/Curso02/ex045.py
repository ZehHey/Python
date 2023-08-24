# Crie um programa que faça o computador jogar Jokenpo com você.

from time import sleep
from random import choice
l = ['PEDRA', 'PAPEL', 'TESOURA']
print('=-' * 40)
print('Vamos jogar Jokenpô.')
print('=-' * 40)
sleep(1)
c = choice(l)
x = str(input('Escolha: pedra, papel ou tesoura: '))
y = x.upper()
print('\033[1;32mEstá pronto?\033[m')
sleep(1)
print('\033[1;35mJO\033[m')
sleep(1)
print('\033[1;35mKEN\033[m')
sleep(1)
print('\033[1;35mPO!!!!\033[m')
print('\033[7m-\033[m' * 20)

print('\033[1;33mPC: {}\033[m'.format(c))
print('\033[1;34mVocê: {}\033[m'.format(y))

print('\033[7m-\033[m' * 20)
if c == 'PEDRA' and y == 'TESOURA':
    print('\033[1;4;31mVocê perdeu.\033[m')
elif c == 'TESOURA' and y == 'PAPEL':
    print('\033[1;4;31mVocê perdeu.\033[m')
elif c == 'PAPEL'and y == 'PEDRA':
    print('\033[1;4;31mVocê perdeu.\033[m')

elif y == 'PEDRA' and c == 'TESOURA':
    print('\033[1;4;32mVocê ganhou.\033[m')
elif y == 'TESOURA' and c == 'PAPEL':
    print('\033[1;4;32mVocê ganhou.\033[m')
elif y == 'PAPEL'and c == 'PEDRA':
    print('\033[1;4;32mVocê ganhou.\033[m')
elif c == y:
    print('\033[1;4;36mEmpatou.\033[m')
