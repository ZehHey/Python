# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, crie duas listas extras, que vão
# conter apenas os numeros pares e os impares digitados. Ao final, mostre o contúdo das 3 listas.
# OBS: (NÃO ALIMENTAR AS TRES LISTAS AO DIGITAR O NUMERO).

num = []
par = []
impar = []
r = 's'
while r == 's':
    n = int(input('Digite um número: '))
    num.append(n)
    r = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    while r != 's' and r != 'n':
        print('Resposta inválida.')
        r = str(input('Deseja continuar? [s/n]: ')).strip().lower()

for v in num:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os números digitados foram: {num}')
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {impar}')
