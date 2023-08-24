# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão.

# 1 para bináio
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número: '))
print('Escolha a base de conversão:')
print('1 para binário;')
print('2 para octal;')
print('3 para hexadecimal.')
e = int(input(''))
if e == 1:
      print('Conversãoo binária: {}'.format(bin(num)[2:]))
elif e == 2:
      print('Conversão octal: {}'.format(oct(num)[2:]))
elif e ==3:
      print('Conversão hexadecimal: {}'.format(hex(num)[2:]))
else:
      print('A opção selecionada não foi reconhecida.')