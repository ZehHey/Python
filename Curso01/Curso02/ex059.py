# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar; [2]multiplicar; [3]maior; [4]novos numeros; [5]sair do programa

x = 4
while x == 4 or x != 5:
    if x == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        print('O que você deseja fazer?'
                  '\n[1] Somar'
                  '\n[2] Multiplicar'
                  '\n[3] Maior'
                  '\n[4] Novos Numeros'
                  '\n[5] Sair')
        x = int(input('R: '))
    elif x == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        print('O que você deseja fazer?'
              '\n[1] Somar'
              '\n[2] Multiplicar'
              '\n[3] Maior'
              '\n[4] Novos Numeros'
              '\n[5] Sair')
        x = int(input('R: '))
    elif x == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        print('O que você deseja fazer?'
              '\n[1] Somar'
              '\n[2] Multiplicar'
              '\n[3] Maior'
              '\n[4] Novos Numeros'
              '\n[5] Sair')
        x = int(input('R: '))
    elif x == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
            print('O que você deseja fazer?'
                  '\n[1] Somar'
                  '\n[2] Multiplicar'
                  '\n[3] Maior'
                  '\n[4] Novos Numeros'
                  '\n[5] Sair')
            x = int(input('R: '))

        else:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n2))
            print('O que você deseja fazer?'
                  '\n[1] Somar'
                  '\n[2] Multiplicar'
                  '\n[3] Maior'
                  '\n[4] Novos Numeros'
                  '\n[5] Sair')
            x = int(input('R: '))
    else:
        print('Opção inválida.')
        x = 4
print ('FIM')