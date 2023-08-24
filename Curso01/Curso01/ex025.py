# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome:

n = str(input('Digite o nome completo: ')).strip()
print('Tem "Silva" no nome?')
n2 = ('SILVA' in n.upper())
if n2 == True:
    print('A resposta é Sim.')
else:
    print('A resposta é NÃO.')