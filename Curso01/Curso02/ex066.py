# Crie um programa que leia varios numeros inteiros. O programa só vai parar quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual a soma entre eles.

cont = soma = 0
while True:
    n = int(input('Digite um número [999 ´para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')