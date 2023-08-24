# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira vai
# sortear 5 números e colocá-los dentro da lista e a segunda vai mostrar a soma entre todos os números pares sorteados
# pela função anterior.

from time import sleep
from random import randint


def sort(lst):
    print('Sorteando 5 valores da lista: ', end='')
    while True:
        n = randint(1, 10)
        if n not in lst:
            lst.append(n)
            sleep(0.3)
            print(f'{n} ', end='')
        if len(lst) == 5:
            break

def soma(lst):
    par = []
    s = 0
    print('\nSomando os valores pares da lista: [', end='')
    for c in lst:
        if c % 2 == 0:
            par.append(c)
            s += c
            print(f' {c} ', end='')
    print(f'] = {s}')


x = []
sort(x)
soma(x)
