# Escreva um numero que faça o computador "pensar" em um numero inteiro entre  e 5 e peça para o usuário tentar
# descobrir qual foi o numero escolhido pelo computador.
# O programa deverá informar se o palpite está certo ou errado.

import random
from time import sleep    # o metodo sleep faz o computador esperar alguns segundos
print('-=-' * 20)
print('Pensei em um numero de 0 a 5.')
n: int = random.randint(0,5)
p = int(input('Digite seu palpite: '))
print('PROCESSANDO...')
sleep(3)
if p == n:
    print('ACERTOU MIZERÁVEL!!')
else:
    print('É... Não foi dessa vez. Eu pensei no {}, e não no {}!'.format(n, p))
print('-=-' * 20)