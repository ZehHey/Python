# faça um programa que leia algo digitado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

n = input('Digite um algo: ')
print('Tipo primitivo: ', type(n))
if(n.isnumeric() == True):
    print(n,' é um numero.')
elif(n.isalpha() == True):
    print(n,' é alfabético.')
elif(n.isalnum() == True):
    print(n, "é alfanumérico.")
else:
    print (n,' é um símbolo')


