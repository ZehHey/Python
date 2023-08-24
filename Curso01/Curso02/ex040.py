# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final
# de acordo com a média atingida:
# - Média abaixo de 5. = reprovado
# - Média entre 5.0 e 6.9 = recuperação
# - Média 7.0 ou superior = aprovado

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
m = float((a + b) / 2)
if m > 7.0:
    print('Sua média é {:.2f}. Parabéns você está \033[1;32mAPROVADO\033[m.'.format(m))
elif m < 5.0:
    print('Sua média é {:.2f}. Infelizmente você está \033[1;31mREPROVADO\033[m.'.format(m))
else:
    print('Sua média é {:.2f}. Você está de \033[1;33mRECUPERAÇÂO\033[m.'.format(m))
