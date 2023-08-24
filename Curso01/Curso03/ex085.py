# Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

numeros = [[], []]
n = 0
for v in range(0, 7):
    n = int(input(f'Digite o {v + 1}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'Os números pares digitados foram {sorted(numeros[0])}')
print(f'Os números ípares digitados foram {sorted(numeros[1])}')
