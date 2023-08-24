# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def escreva(msg):
    a = (len(msg) + 10)
    print('~' * a)
    print(f'     {msg}')
    print('~' * a)


txt = str(input('Digite o texto: '))
escreva(txt)
txt = str(input('Digite o texto: '))
escreva(txt)
txt = str(input('Digite o texto: '))
escreva(txt)

