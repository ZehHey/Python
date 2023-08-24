# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['Idade'] = (date.today().year - ano)
ct = int(input('CTPS (0 caso não tenha): '))
if ct != 0:
    dados['CTPS'] = ct
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    ap = (dados['Ano de contratação']) + 35
    dados['Aposentadoria'] = (ap - ano)
print()
print('-=' * 15)
for k, v in dados.items():
    print(f'    -{k}: {v}')