# Melhore o ex061, perguntando se o usuario quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos

pt = int(input('Pimeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
x = 10
while x != 0:
    total += x
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('...')
    print('Deseja mostrar mais quantos termos:')
    x = int(input('R: '))
print('{} termos foram exibidos.'.format(total))
print('FIM!')