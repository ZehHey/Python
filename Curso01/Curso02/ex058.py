# Melhore o jogo ex028 onde o computador vai "pensar" em um número entre 0 a 10. só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint
pc = 0
user = 1
soma = 0
print('-=-=-=-=- ADIVINHE O NÚMERO --=-=-=-')
print('PC: \033[1;35mVou pensar em um número de 1 a 10.\033[m')
pc = randint(1, 10)
sleep(1)
print('PC: \033[1;35mPENSANDO\033[m')
sleep(2)
print('PC: \033[1;35mPronto... Qual o seu palpite?')
user = int(input('R: '))
while user != pc:
    soma += 1
    if user < pc:
        print('PC: \033[1;35mVoce \033[31merrou\033[m\033[1;35m, tente um número maior.\033[m')
        print('PC: \033[1;35mPronto?? Qual o seu palpite?\033[m')
        user = int(input('R: '))
    if user > pc:
        print('PC: \033[1;35mVoce \033[31merrou\033[m\033[1;35m, tente um número menor.\033[m')
        print('PC: \033[1;35mPronto?? Qual o seu palpite?\033[m')
        user = int(input('R: '))
soma += 1
print('PC: \033[1;35mVocê \033[32;1macertou\033[m\033[1;35m!!!\033[m \nPC: \033[1;35mEu pensei exatamente no número {}.'
      '\n\033[mPC: \033[1;35mVocê precisou de {} palpites\033[m'.format(pc, soma))
print('FIM!!')
