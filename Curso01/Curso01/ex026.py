# Crie um pograma que leia uma frase e mostre:
# * Quantas vezes aparece a letra "A";
# * Em que posição ela aparece a primeira vez;
# * Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
f = frase.lower()
a = f.count('a')
print('A letra "A" aparece {} vezes na frase digitada.'.format(a))
print('A primeira letra"A" apareceu na posição {}'.format(f.find('a')+1))
print('A ultima letra "A" apareceu na posição {}'.format(f.rfind('a')+1))
