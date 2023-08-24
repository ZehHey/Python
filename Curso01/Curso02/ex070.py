# Crie um programa que leia o nome e o preço de varios produtos. O programa deve perguntar se o usuário vai continuar.
# No final mostre:
# 1 - O total gasto na compra;
# 2 - Quantos produtos custam mais de R$1000.00;
# 3 - Qual o nome do produto mais barato.

total = caro = cont = barato = 0
prodbar = ''
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if cont == 1:
        menor = preço
        prodbar = produto
    if preço < menor:
        menor = preço
        prodbar = produto
    r = str(input('Cadastrar mais? [s/n]')).strip().lower()[0]
    if preço >= 1000:
        caro += 1
    if r != 's' and r != 'n':
        r = str(input('Opção inválida. Deseja cadastrar mais? [s/n]: ')).strip().lower()[0]
    if r == 'n':
        break
print(f'O total da compra é de R${total:.2f}.')
print(f'{caro} produtos custa(m) mais de R$1000.00.')
print(f'O produto mais barato é {prodbar} e custa R${menor:.2f} ')
