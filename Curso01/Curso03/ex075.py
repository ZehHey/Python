#  Crie um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o número 9
# B) Em que posição foi digitado o numero 3
# C) Quais são os números pares.

num = (int(input('Digite um numero: ')), int(input('Digite  mais um numero: ')),
       int(input('Digite um outro numero: ')), int(input('Digite um ultimo numero: ')), )
print(f'Você digitou os numeros {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3) + 1}ª posição')
else:
    print('-------------')
print(f'Os números pares digitados foram: ',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('')
