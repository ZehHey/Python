# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

r = 's'
sex = 'M'
while r == 's' and sex == 'M' or sex == 'F':
    print('-=' * 20)
    name = str(input('Nome: ')).strip().title()
    sex = str(input('Sexo [M/F]')).strip().upper()[0]
    while sex != 'M' and sex != 'F':
        sex = str(input('Opção invalida. Digite novamente o sexo [M/F]: ')).upper()
    if sex == 'M' or sex == 'F':
        r = str(input('Deseja continuar? [s/n]'))

print('FIM')