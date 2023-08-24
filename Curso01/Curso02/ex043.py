# Faça um programa que receb o peso e altura do usuário e calcule seu IMC, mostrando seu status:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso;
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade Mórbida

a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
c = float(p / (a * a))
print('Seu IMC é de: \033[4m{:.1f}\033[m.'.format(c))
if c < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO\033[m.')
elif 18.5 <= c < 25:
    print('Você está no \033[1;32mPESO IDEAL\033[m.')
elif 25 <= c < 30:
    print('Você está com \033[1;34mSOBREPESO\033[m.')
elif 30 <= c < 40:
    print('Você está com \033[1;33mOBESIDADE\033[m.')
else:
    print('Você está com \033[1;31mOBESIDADE MORBIDA\033[m.')
