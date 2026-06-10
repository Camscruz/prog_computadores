"""
2) [2,0 pontos] Escreva uma função que recebe como parâmetros os três
    inteiros L1, L2 e L3, representando os três lados de um triângulo, e
    retorna 1, se o triângulo é escaleno, 2, se o triângulo é isósceles,
    ou 3, se o triângulo é equilátero.

Considere o seguinte protótipo para a função:
def tipo_triangulo(L1: int, LL2: int, LL3: int) -> int:
"""

def tipo_triangulo(l1, l2, l3):
    if l1==l2 and l1==l3 and l2==l3:
        return 3
    elif l1!=l2 and l1!=l3 and l2!=l3:
        return 1
    else:
        return 2
    
l1=int(input("Insira um valor para l1: "))
l2=int(input("Insira um valor para l2: "))
l3=int(input("Insira um valor para l3: "))

print(tipo_triangulo(l1, l2, l3))


