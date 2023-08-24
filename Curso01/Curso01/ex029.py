# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite

print('Qual a velocidade do carro?')
v = int(input('R: '))
if v > 80:
    print('-' * 70)
    print('Você está acima da velocidade pemitida e será multado em R${:.2f}.'.format((v - 80) * 7))
    print('-' * 70)
else:
    print('-' * 37)
    print('Você está dentro do limite permitido.')
    print('-' * 37)
