# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - até 14 anos: Infantil
# - até 19 anos: Junior
# - até 30 anos: Senior
# - Acima: Master

from datetime import date
aa = date.today().year
n = int(input('Digite o ano de nascimento: '))
i = int(aa - n)
print('Conforme a idade de {} anos, a categoria a qual se enquadra é:'.format(i))
if i <= 9:
    print('\033[1;34mMirim\033[m.')
elif 9 < i <= 14:
    print('\033[1;34mInfantil\033[m.')
elif 14 < i <= 19:
    print('\033[1;34mJunior\033[m.')
elif 19 < i <= 30:
    print('\033[1;34mSenior\033[m.')
elif i > 30:
    print('\033[1;34mMaster\033[m.')