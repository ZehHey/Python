# Elabore um programa que calcule o valor a ser pago por um poduto, considerando o
# seu preço normal e a condição de pagamento
# - À vista dinheiro ou cheque - 10% de desconto
# - À vista no cartão - 5% de desconto
# - Até 2x no cartão - preço normal
# - 3 x ou mais no cartão 20% de juros

p = float(input('Digite o valor da compra: R$'))
print('''Considerando:
1 - Dinheiro.
2 - Cheque
3 - Cartão''')
f = int(input('Qual a forma de pagamento: '))
v = int(input('Em quantas parcelas (Considerando 0 como à vista.):'))
cinco = (p * 5 / 100)
dez = (p * 10 / 100)
vinte = (p * 20 /100)
if f == 1 or f == 2 and v == 0:
    print('Nessas condições você paga R${:.2f}'.format(p - dez))
elif v == 0 and f == 3:
    print('Nessas condições você paga R${:.2f}'.format(p - cinco))
elif f == 3 and v <= 2:
    print('Nessas condições você paga R${:.2f}'.format(p))
    print('Com {:.0f} parcelas de R${:.2f}.'.format(v, (p / v)))
elif f == 3 and v > 2:
    print('Nessas condições você paga R${:.2f}'.format(p + vinte))
    print('Com {:.0f} parcelas de R${:.2f}.'.format(v, (p + vinte) / v))
else:
    print('Não foi possível calcular.')
