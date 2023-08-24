# Reescreva a função leiaInt() do ex114, incluindo agora a possibilidade da digitação de um número de tipo
# inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

import modulos
nin = modulos.leiaInt('Digite um número inteiro: ')
nfl = modulos.leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {nin} e o real foi {nfl:.2f}')
