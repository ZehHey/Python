# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço FOR

n = int(input('Digite um número: '))
print('')
print('=-' * 9)
print('A tabuada do {} é:'.format(n))
for c in range (1, 11):
    print(f'{n} x {c:2} = {c*n}')
print('=-' * 9)
