# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções
# utilizadas nos exercícios anteriores para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda, dado

p = float(input('Digite um preço: R$'))
moeda.resumo(p, 35, 22)
