"""
3) [3,0 pontos] Escreva uma função que recebe como parâmetros um vetor de números inteiros V e
um número inteiro N e retorna um novo vetor em que equivale ao anterior com cada elemento
multiplicado por N.

Por exemplo, se V = [1, 3, 4] e N = 2, a função retornaria o vetor [2, 6, 8].

Considere o seguinte protótipo para a função:

def mult_vet_N(V: list[int], N: int) -> list[int]
"""

def mult_vet_N(V, N):
    V2 = []
    for i in range(len(V)):
    V2.append(V[i]*N)
return V2