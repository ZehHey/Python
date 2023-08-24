# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício ,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('...')
sleep(0.5)
print('ATENÇÃO PARA A CONTAGEM REGRESSIVA.')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(.5)
print('\033[1;31mFOGOS\033[m')