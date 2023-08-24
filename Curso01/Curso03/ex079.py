# Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados em ordem crescente.

a = 's'
num = []
while a == 's':
    n = int(input('Digite um valor: '))
    if n in num:
        print('Valor ja digitado.')
    else:
        num.append(n)
    a = str(input('Deseja continuar? [s/n]: ')).lower().strip()
    while a != 's' and a != 'n':
        a = str(input('Não entendi. Deseja continuar:'))

num.sort()
print('')
print(f'Os números digitados foram: {num}')
