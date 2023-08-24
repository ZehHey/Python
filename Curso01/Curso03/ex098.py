# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.Seu programa
# tem que realizar três contagens através da função criada:
# A) de 1 até 10, a cada 1;
# B) de 10 até 0, a cada 2;
# C) uma contagem personalizada


from time import sleep


def lin():
    print('-=' * 15)


def contador(x, y, z):
    if x < y:
        cont = x
        while cont <= y:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += z
    else:
        cont = x
        while cont >= y:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= z

lin()
print('Contador de 1 ao 10, a cada 1:')
contador(1, 10, 1)
print()
sleep(0.5)
lin()
print('Contador de 10 ao 2, a cada 2:')
contador(10, 0, 2)
print()
lin()
print('Contador personalizado')
a = int(input('Digite o início: '))
b = int(input('Digite o fim: '))
c = int(input('Digite o passo: '))
if c == 0:
    c = 1
elif c < 0:
    c *= -1
print()
contador(a, b, c)
