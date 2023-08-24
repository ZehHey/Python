# Faça um programa que leia um número inteiro e diga se é ou não um número primo
count = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
        if n % c == 0:
            count += 1
if count == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo, ele é multiplo de {} valores.'.format(n, count))

print('FIM')
