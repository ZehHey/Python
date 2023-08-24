# Crie um progama que leia o nome d e uma cidade e diga se ela começa ou não com o nome 'Santo':

c = str(input('Digite o nome da cidade: ')).strip()
print('O nome da sua cidade começa com Santo?')
d = (c[:5].upper() =='SANTO')
if d == True:
    print('Sim.')
else:
    print('Não.')

#c2 = c.find('Santo')
#if c2 == 0:
 #   print('Sim.')
#else:
 #   print('Não.')
