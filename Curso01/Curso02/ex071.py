# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário o valor a ser sacado.
# Então o programa deve informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui notas de R$50, R$20, R$10 e de R$1.

'''R50 = R20 = R10 = R1 =  0
while True:
    saque = int(input('Valor do saque: '))
    un = saque // 1 % 10
    de = saque // 10 % 10
    ce = saque // 100 % 10
    mi = saque // 1000 % 10
    if ce > 0:
        if ce < 3:
            for c in range (0, ce):
                R20 += 5
        if ce >3:
            for c in range(0, ce):
                R50 += 2
    if mi > 0:
        for c in range(0, mi):
            R50 += 20
    if de > 0:
        x = de % 2
        if x == 0:
            for c in range(0, de, 2):
                R20 += 1
        else:
            for c in range (0, de):
                R10 += 1
    if un > 0:
        for c in range(0, un):
            R1 += 1
    r = str(input('Deseja ralizar mais um saque? [s/n]: ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Você sacou R${saque:.2f}')
print(f'Um total de {R50} notas de R$50, {R20} notas de R$20, {R10} notas de R$10 e {R1} notas de R$1.')
print('Fim')'''

soma = r1 = r10 = r20 = r50 = 0
while True:
    v = int(input('Quanto deseja sacar? R$'))
    r = str(input('Contiuar [s/n]? ')).strip().lower()
    while r != 's' and r != 'n':
        r = str(input('Contiuar [s/n]? ')).strip().lower()
    soma += v
    if r == 'n':
        break
un = soma // 1 % 10
de = soma // 10 % 10
ce = soma // 100 % 10
mi = soma // 1000 % 10
if ce > 0:
    for c in range (0, ce):
        r50 += 2
if de == 5:
    r50 += 1
if mi > 0:
    for c in range (0, mi):
        r50 += 20
if de < 5:
    if de % 2 == 0:
        for c in range (0, de, 2):
            r20 += 1
    else:
        for c in range (0, de):
            r10 +=1
if de > 5:
    r50 += 1
    if (de - 5) % 2 == 0:
        for c in range (0, de - 5, 2):
            r20 += 1
    else:
        for c in range (0, de):
            r10 +=1
if un > 0:
    for c in range (0, un):
        r1 += 1
if r50 >0:
    print(f'Notas de R$50: {r50}')
if r20 > 0:
    print(f'Notas de R$20: {r20}')
if r10 > 0:
    print(f'Notas de R$10: {r10}')
if r1 > 0:
    print(f'Notas de R$1: {r1}')