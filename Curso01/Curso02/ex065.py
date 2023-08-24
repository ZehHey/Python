# Crie um programa que leia varios numeros inteiros. No final da execução, mostre o maior, o menor e a média
# entre todos os valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

r = 's'
cont = soma = media = maior = menor = 0
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Desena continuar? [s/n]: ')).lower().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Você digitou {} números.'.format(cont))
print('A soma entre eles é {}.'.format(soma))
print('A média entre eles é {:.2f}.'.format(media))
print('Maior {}'.format(maior))
print('menor {}'.format(menor))
