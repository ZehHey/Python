# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Obs: use cores.

from time import sleep
c = ('\033[m',          # 0 — sem cores
     '\033[0;30;41m',   # 1 — vermelho
     '\033[0;30;42m',   # 2 — verde
     '\033[0;30;43m',   # 3 — amarelo
     '\033[0;39;44m',   # 4 — azul
     '\033[0;30;45m',   # 5 — roxo
     '\033[7;40m'       # 6 — branco
)


def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'', 4)
    print(c[6],end='')
    help(cmd)
    print(c[0],end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


com = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    com = str(input('Função ou Biblioteca > '))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
titulo('VOLTE SEMPRE', 5)