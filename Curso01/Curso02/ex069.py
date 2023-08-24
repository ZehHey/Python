# Crie um pprograma que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá peguntar
# se o usuario quer ou nao continuar. No final,mostre:
# 1 - Quantas pessoas tem mais de 18 anos.
# 2 - Quantos homens foram cadastrados.
# 3 - Quantas mulheres tem menos de 20 anos

total = maiores = homens = mulheres = 0
while True:
    nome = str(input('Digite o nome: ')).strip().title()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida. Digite o sexo [M/F]:')).strip().upper()[0]
    idade = int(input('Idade: '))
    total += 1
    r = str(input('Deseja cadastrar outra pessoa? [s/n]')).strip().lower()[0]
    if idade >=18:
        maiores += 1
    if sexo =='M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if r != 's' and r != 'n':
        r = str(input('Opção inválida. Deseja continuar? [s/n]: ')).strip().lower()[0]
    if r == 'n':
        break
print(f'{total} pessoas foram cadastradas.')
print(f'{maiores} pessoas são maiores de 18 anos.')
print(f'{homens} pessoas são homens.')
print(f'{mulheres} pessoas são mulheres com idade abaixo dos 20 anos.')
