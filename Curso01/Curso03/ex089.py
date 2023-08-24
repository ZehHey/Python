# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada aluno e permita que o usuário possa mostrar as notas de cada um dos alunos
# individualmente.

todos = []
soma = 0
while True:
     nome = str(input('Aluno: ')).title().strip()
     n1 = float(input('Nota 01: '))
     n2 = float(input('Nota 02: '))
     media = (n1 + n2) / 2
     todos.append([nome, [n1, n2], media])
     r = str(input('Deseja continuar? [s/n]: ')).strip().lower()
     soma += 1
     if r == 'n':
         break
print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-' * 26)
for i, a in enumerate(todos):
     print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
     print('-' * 35)
     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
     if opc == 999:
         print('FINALIZANDO...')
         break
     if opc <= len(todos):
          print(f'Notas de {todos[opc-1][0]} são {todos[opc-1][1]}')
