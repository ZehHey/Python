# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionario, incluindo o total de gols feitos durante o campeonato.

a = {}
gols = []
tot = 0
a['Nome'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input('Número de partidas jogadas: '))
for n in range(1, partidas +1):
    g = int(input(f'Quantos gols marcados na {n}ª partida: '))
    gols.append(g)
    tot += g
a['Gols'] = gols
a['Total'] = tot

print(f'O jogador {a["Nome"]} jogou {partidas} partidas.')
for c in range(1, partidas + 1):
    print(f'    => Na {c}ª partida, ele marcou {gols[c - 1]} gols.')
print(f'Foi um total de {tot} gols, com uma média de {tot/partidas} gols por jogo.')