# Crie um pequeno sistema modularizado que permitacadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções:
# A) Cadastrar uma nova pessoa
# B) Listar todas as pessoas cadastradas.

from formatacao import *
from arquivo import *
from time import sleep
arq = 'cad.txt'
while True:
    titulo('MENU PRINCIPAL')
    menu(1, 'Mostrar pessoas cadastradas')
    menu(2, 'Cadastrar nova pessoa')
    menu(3, 'Sair')
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    sleep(2)
    if opc == 1:
        titulo('Lista de cadastrados')
        ler(arq)
        sleep(2)
    elif opc == 2:
        nome = str(input('Nome: ')).strip().title()
        escrever(f'{nome:<43}')
        idade = leiaInt('Idade: ')
        escrever(f'{idade} anos\n')
        print(f'Registro "{nome}" adicionado com sucesso.')
        sleep(2)
    elif opc == 3:
        print('opcao 3')
        break
    else:
        print('\033[31mOpção Inválida.\033[m')

