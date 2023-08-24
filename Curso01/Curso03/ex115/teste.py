with open('cad.txt', 'w') as arq:
    arq.write('teste de escrita')

with open('cad.txt', 'a') as arq:
    arq.write('\nSegunda linha.')
with open('cad.txt', 'r') as arq:
    a = arq.read()
    print(a)