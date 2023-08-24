# Faça um programa que leia o peso de cinco pessoas e no final, mostre qual foi o maior
# e o menor peso.

maior = 0
nmaior = 0
menor = 0
nmenor = 0
for c in range (1, 6):
    p = float(input(f'Digite o peso da {c}ª pessoa (Kg): '))
    if c == 1:
        maior += p
        nmaior += c
        menor += p
        nmenor += c
    else:
        if p > maior:
            maior = p
            nmaior = c
        if p < menor:
            menor = p
            nmenor = c
print(f'O maior peso registrado foi o {nmaior}º de {maior}Kg.')
print(f'O menor peso registrado foi o {nmenor}º de {menor}Kg.')