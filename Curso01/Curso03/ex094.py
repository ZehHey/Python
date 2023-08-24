# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada um em um dicionário e todos
# os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma lista com todas as mulheres;
# c) Uma lista com todas as pessoas com idade acima da média.

dados = {}
todos = []
mul = []
mai = []
tot = soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().capitalize()[0]
    while dados['Sexo'] not in 'MF':
        print('Dado inválido.')
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().capitalize()[0]
    if dados['Sexo'] == 'F':
        mul.append(dados['Nome'])
    dados['Idade'] = int(input('Idade: '))
    mai.append(dados['Idade'])
    soma += dados['Idade']
    tot += 1
    todos.append(dados.copy())
    r = str(input('Deseja continuar?[s/n] ')).strip().lower()
    while r not in 'sn':
        print('Resposta inválida.')
        r = str(input('Deseja continuar?[s/n] ')).strip().lower()
    if r == 'n':
        break
media = (soma / tot)
print('-=' * 30)
print(f'     => Total de pessoas cadastradas = {tot}')
print(f'     => Média de idade = {media:.1f}')
print('     => Pessoas com idade acima da média = ')
for c in range(0, len(todos)):
    if todos[c]['Idade'] >= media:
        print(f'        Nome: {todos[c]["Nome"]} - Idade: {todos[c]["Idade"]}')
print('     => Mulheres cadastradas = ', end='')
for c, v in enumerate(mul):
    print(f'{v} - ', end='')
print()
