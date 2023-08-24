def leiaInt(num):
    ok = False
    while not ok:
        try:
            n = str(input(num))
            a = int(n)
            ok = True
            return a
        except (ValueError, TypeError):
            print(f'\033[1;4;31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            ok = True
            return 0


def leiaFloat(num):
    ok = False
    while not ok:
        try:
            n = str(input(num)).replace(',', '.')
            a = float(n)
            ok = True
            return a
        except (ValueError, TypeError):
            print(f'\033[1;4;31mErro! Digite um número real válido.\033[m')
        except (KeyboardInterrupt, GeneratorExit):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            ok = True
            return 0