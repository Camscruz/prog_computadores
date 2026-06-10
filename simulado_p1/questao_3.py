# Escreva um programa que receba de entrada 3 números representado as dimensões dos 3 lados de um triângulo
# e indique se esse triângulo é equilátero ou não.
# Considere que sempre serão fornecidos números válidos.

# Entrada dos lados do triângulo
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# Verificação se é equilátero
if a == b == c:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")
