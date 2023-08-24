# Crie um programa que leia varios numeros inteiros. O programa só deve parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e a soma entre eles.

n = cont = soma = 0
n = int(input('Digite o numero: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite o numero: '))

print('Você digitou {} valores e a soma deles é {}'. format(cont, soma))