# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o praço da passagem cobrando R$0.50 por km para viagens até 200Km e R$0.45 para viagens mais longas

print('Qual a distância em Km?')
d = float(input('R: '))
if d <= 200:
    print('-' * 35)
    print('Sua passagem custará R${:.2f}.'.format(d * 0.50))
else:
    print('-' * 35)
    print('Sua passagem custará R${:.2f}.'.format(d * 0.45))
print('-' * 35)
