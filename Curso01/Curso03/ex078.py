# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


num = []
pma = []
pmi = []
for c in range(0, 5):
    num.append(int(input(f'Digite o valor da posição {c}: ')))
ma = max(num)
mi = min(num)
for p, cont in enumerate(num):
    if cont == ma:
        pma.append(p)
    if cont == mi:
        pmi.append(p)
print(f'Os valores digitados são: {num}')
print('')
print(f'O maior valor digitado é {max(num)} e está nas posições: {pma}')
print(f'O menor valor digitado é {min(num)} e está nas posições: {pmi}')
