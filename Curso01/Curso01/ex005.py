# Operações aritméticas
# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

n1 = int(input("Digite um número:"))
n2 = int(input('Digite outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2
print("A some é {}, o produto é {} e a divisão é {}".format(s, m, d), end=" ")
print("A potência é {}, a divisão inteira é {}, e o resto da divisão é {}".format(e, di, rd))


