try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os dados digitados.')
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por 0.')
except KeyboardInterrupt:
    print('Dado não informado.')
else:
    print(f'O resultado é {r:.2f}')
