# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados;
# B) Todos valores em ordem decrescente;
# C) Se o valor 5 foi digitado e está ou não na lista


num = []
cont = 0
r = 's'
while r == 's':
    n = int(input('Digite um número: '))
    num.append(n)
    cont += 1
    r = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    while r != 'n' and r != 's':
        print('Resposta inválida.')
        r = str(input('Deseja continuar? [s/n]: ')).strip().lower()
num.sort(reverse=True)
print('')
print(f'Você digitou {cont} numeros.')
print(f'Os valores digitados foram: {num}')
if 5 in num:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')