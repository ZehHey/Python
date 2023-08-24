# Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual é o maior.

from random import randint


def maior(dados):
    c = randint(1, 7)
    dados = []
    while len(dados) < c:
        n = randint(1, 10)
        if n not in dados:
            dados.append(n)
    a = max(dados)
    print('-=' * 15)
    print('Analisando valores informados...')
    print(f'{dados}')
    print(f'Foram informados {len(dados)} valores.')
    print(f'O maior valor informado foi {a}')
    print()


x = []
maior(x)
y = []
maior(y)
z = []
maior(z)
w = []
maior(w)
k = []
maior(k)


# Solução real da aula

'''def maior(* num):
    cont = maior = 0
    print('\nAnalizando...')
    for n in num:
        print(f'{n} ', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''