# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados;
# B) Os ultimos 4 colocados;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o time que o usuário pesquisar.

print('-=-=-=-= \033[4mTABELA FINAL CAMPEONATO BRASILEIRO 2022\033[m =-=-=-=-')

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico', 'Atletico - MG', 'Fortaleza',
         'São Paulo', 'America - MG', 'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara', 'Atletico - GO',
         'Avai', 'Juventude')
print('')
print('-=' * 20)
print('Os 5 primeiros colocados são:')
for c in range(0,5):
    print(f'{c + 1}º - {times[c]}')
print('-=' * 20)

print('Os 4 últimos colocados são:')
for c in range(16,20):
    print(f'{c + 1}º - {times[c]}')
print('-=' * 20)
print('')

print('Aqui estão os 20 clubes organizados em ordem alfabética:')
for c in sorted(times):
    print(c)
print('-=' * 20)


print('Deseja  saber a colocação de qual time?')
clube = str(input('Clube: ')).title().strip()
print('')
print(f'O {clube} está na {times.index(clube) + 1}ª posição')
print('-=' * 20)
