# Aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

todos = []
dados = {}
gols = []
while True:
    dados['Nome'] = str(input('Nome do jogador: ')).title()
    n = int(input('Nº de partidas: '))
    for c in range(1, n+1):
        gols.append(int(input(f'    Nº de gols na {c}ª partida: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    todos.append(dados.copy())
    gols.clear()
    r = str(input('Deseja continuar?[s/n]: ')).lower().strip()[0]
    if r not in 'sn':
        print('Resposta inválida.')
        r = str(input('Deseja continuar?[s/n]: ')).lower().strip()[0]
    if r == 'n':
        break
print('=-' * 30)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}{"Total":>6}')
print('-'*60)
for p, d in enumerate(todos):
        print(f'{p:<4}',end='')
        for x in d.values():
            print(f'{str(x):<15}', end='')
        print()
while True:
    c = int(input('Mostrar os dados de qual jogador? (999 para encerrar): '))
    if c == 999:
        print('ENCERRANDO...')
        break
    elif c < len(todos):
        print(f' --LEVANTAMENTO DO JOGADOR {(todos[c]["Nome"])}:')
        for c, g in enumerate(todos[c]['Gols']):
            print(f'No jogo {c+1} fez {g} gols.')
    else:
        print('Não encontrei o jogador cadastrado com esse código.')
        c = int(input('Mostrar os dados de qual jogador? (999 para encerrar): '))
    print('-' * 60)
