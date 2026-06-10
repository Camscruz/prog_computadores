"""
4) [3,0 pontos] Escreva uma função que receba uma string S e um inteiro N como parâmetros e retorna
uma nova string com a letra na posição N removida da string. Se não existir a posição N na string, a
função deve retornar a string original. Por exemplo, se fosse fornecida a string ‘Arte’ e o inteiro 1, a
função retornaria “Ate”. Considere o seguinte protótipo para a função:

def remove_n( S:str , N:int ) - > str
"""

def remove_n(S, N):
    R = ""
  for i in range(len(S)):
    if (i != N):
      R = R + S[i]
  return R