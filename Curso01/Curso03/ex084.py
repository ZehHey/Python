# Faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mas leves

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')).capitalize().strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    if resp in 'n':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas,')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')