# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
# O comando \n quebra a linha do código
# O Comando :.2f serve para deixar apenas 2 casas decimais em um numero composto
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('seu dobro é {} , \nseu triplo é {} \ne sua raiz quadrada é {:.2f}.' .format(d, t, r))
