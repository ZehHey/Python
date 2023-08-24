# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.0, o aumento é de 10%
# Para os inferiores, o aumento é de 15%.

print('Digite seu salário.')
s = float(input('R: '))
if s >= 1250.0:
    a1 = s * (10/100)
    a2 = s + a1
    print('Seu aumento é de 10%, R${:.2f}, seu novo salário é R${:.2f}'.format(a1, a2))
else:
    b1 = s * (15/100)
    b2 = s + b1
    print('Seu aumento é de 15%, R${:.2f}, seu novo salário é R${:.2f}'.format(b1, b2))
print('-' * 50)
