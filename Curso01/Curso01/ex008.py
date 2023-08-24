#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Digite a medida em metros: '))
c = m * 100
mm = m * 1000
print('O valor em cm é {} e o valor em mm é {}'. format(c, mm))
