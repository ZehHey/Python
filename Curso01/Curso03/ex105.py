# Faça um programa que tenha uma função chamada notas() que pode receber várias notas e vai retornar um dicionário com
# as seguintes informações:
# - Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - A situação (opcional)
# Adicione também as docstrings da função.


def notas(*n, sit='False'):
    """
    -->Função paraanalisar notas e situação de vários alunos.
    :param n: notas cadastradas
    :param sit: valor opcional, exibir ou nãoa situação
    :return: dicionário com várias informações e situação da turma.
    """
    media = float(sum(n)/len(n))
    a = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': f"{media:.2f}"}
    if media > 7:
        s = 'ÓTIMA'
    elif media < 5:
        s = 'RUIM'
    else:
        s = 'BOA'
    if sit:
        a['Situação'] = s
    return print(a)


resp = notas(5.5, 2.5, 7.5, 8.5, sit=True)
