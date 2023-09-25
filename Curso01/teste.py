senha = 'Zeh1312'
senha = senha.strip()
senhaoculta = ''

for c in range(0, len(senha)):
    if c == 0 or c == len(senha)-1:
        senhaoculta += senha[c]
    else:
        senhaoculta += '*'


print(senha)
print(senhaoculta)
