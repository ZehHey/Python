# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print(f'{"TABELA DE PREÇOS":^30}')
print('-' * 30)
for c in range(0, len(itens)):
    if c % 2 == 0:
        print(f'{itens[c]:.<20}', end='')
    else:
        print(f'R$ {itens[c]:>6.2f}')
print('-' * 30)
