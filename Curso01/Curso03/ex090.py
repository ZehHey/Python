# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionaário. No final,
# mostre o conteúdo da estrutura na tela.

dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['Situação'] = 'APROVADO(A)'
elif 5 <= dados['média'] < 7:
    dados['Situação'] = 'RECUPERAÇÃO'
else:
    dados['Situação'] = 'REPROVADO(A)'
print(f'Aluno: {dados["nome"]} \n'
      f'Média {dados["média"]} \n'
      f'Sitação: {dados["Situação"]}')