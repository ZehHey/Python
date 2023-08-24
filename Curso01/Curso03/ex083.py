# Crie um programa onde o usuário digite uma expressão matematica qualquer que use parenteses.
# O programa deverá analisar se a expressão está com os parenteses abertos e fechados na ordem correta.

a = []
m = str(input('Digite a expressão matemática: '))
for c in m:
    if c == '(':
        a.append(c)
    elif c == ')':
        if len(a) > 0:
            a.pop()
        else:
            a.append(c)
            break

if len(a) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')