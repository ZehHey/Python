# Dedntro do módulo chamado dado, crie uma função chamada leiaDinheiro() que sejacapazde funcionar como a função
# input(), mas com uma validaçãode dados para aceitar apenas valores que sejam monetários.

from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(p, 35, 22)
