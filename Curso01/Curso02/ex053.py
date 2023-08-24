# Crie um programa que leia uma frase qualque e diga se ela é um PALINDROMO., desconsiderando
# os espaços.

f = str(input('Digite um frase qualquer: ')).strip().upper()
b = f.split()
c = ''.join(b)
i = ''
for letra in range(len(c) - 1, - 1, -1):
    i += c[letra]
if i == c:
    print('O inverso de {} é \033[1;32m{}\033[m'.format(c, i))
    print('Temos um PALINDROMO.')
else:
    print('O inverso de {} é \033[1;31m{}\033[m'.format(c, i))
    print('A frase não é um PALINDROMO.')
