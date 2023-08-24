# Refaça o desafio #51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# prograssão usando a estrutura while.

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    cont +=1
print('FIM!')
