# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimeno de uma pessoa,
# retornando uma valorliteral indicado se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    i = date.today().year - ano
    if i < 16:
        return f'Com {i} anos o voto é: NEGADO'
    elif 65 > i >= 18:
        return f'Com {i} anos o voto é: OBRIGATÓRIO'
    else:
        return f'Com {i} anos o voto é: OPCIONAL'


n = int(input('Em que ano você nasceu? '))
print(f'{voto(n)}')
