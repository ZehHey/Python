# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final. mostre os 10 primeiros termos dessa progressão.
s = 0
p = int(input('Digite o pimeiro termo: '))
r = int(input('Digite a razão:'))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c)
