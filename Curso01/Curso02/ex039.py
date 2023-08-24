# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é hora de se alistar;
# - Se já passou o tempo do alistamento.
# o programa tambem deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date
n = int(input('Digite o ano de nascimento: '))
aa = date.today().year
i = aa - n
print('Você tem {} anos.'.format(i))
if i < 17:
    print('Ainda não chegou a hora de se alistar, ainda faltam {} anos.'.format(17 - i))
elif i == 17:
    print('Esse é o seu ano de alistamento militar.')
elif i == 18:
    print('Seu alistamento era pra ter sido realizado no ano passado.')
else:
    print('Seu prazo de alistamento ja passou a {} anos.'.format(i - 17))