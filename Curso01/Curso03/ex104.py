# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input(), só que fazendo
# a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')


def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!\033[m')
            print('Digite um valor inteiro')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

#-------------------------------------------------------------
'''Solução que encontrei:
def leiaInt(n):
    n = input('Digite um valor inteiro: ').strip()
    while True:
        if n.isalpha():
            print('ERRO!')
            n = input('Digite um valor inteiro: ').strip()
        else:
            a = float(n)
            if a // 1 != a:
                print('ERRO!')
                n = input('Digite um valor inteiro: ').strip()
            else:
                break
            break
    print(f'Você digitou o valor {n}')
    print('FIM!')


a = 0
leiaInt(a)'''
#----------------------------------------------------------------------------------------------------------