# Escreva um programa que receba de entrada 2 inteiros m e n, ambos maiores que 1,
# e imprime o máximo divisor comum (MDC) destes números.
# Considere que sempre serão fornecidos números válidos.

# Entrada dos valores
m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

# Algoritmo de Euclides
while n != 0:
    resto = m % n
    m = n
    n = resto

# Resultado
print("O MDC é:", m)
