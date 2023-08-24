def escrever(msg):
    with open('cad.txt', 'a', encoding='utf-8') as arq:
        arq.write(msg)


def ler(nome):
    with open('cad.txt', 'r', encoding='utf-8') as name:
        print(name.read())
