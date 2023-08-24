# Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print(f'-=-=-= TABUADA DO {n} =-=-=-')

    for c in range(1, 10):
        print(f'{n} x {c} = {n * c}')
    print('-=' * 20)
print('Gerador de tabuada encerrado.')

