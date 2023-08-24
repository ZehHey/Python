# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final mostre:
# 1 - A média de idade do grupo;
# 2 - Qual o nome do homem mais velho.
# 3 - Quantas mulheres tem menos de 20 anos.

si = 0
med = 0
m = 0
old = 0
nold = ''
for c in range(1, 5):
    print('=' * 20)
    print('{}ª PESSOA'.format(c))
    n = str(input('Nome: ')).title().strip()
    i = int(input('Idade: '))
    s = str(input('Sexo?(M/F): ')).upper().strip()
    si += i
    if c == 1 and s == 'M':
        old = i
        nold = n
    if s == 'M' and i > old:
        old = i
        nold = n
    if s == 'F' and i < 20:
        m += 1
med = si / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(med))
print('O homem mais velho tem {} anos e se chama {}.'.format(old, nold))
print('O Total de mulheres abaixo de 20 anos é: {}'.format(m))

