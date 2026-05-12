# Nome: Camille Cardoso Cruz - Turma: J1
# Aula prática 05

# Faça um programa que lê um vetor de 5 elementos e imprime na tela a média dos valores do vetor e o valor mais próximo da média. 
# Exemplo: Se for fornecido o vetor [2.5, 7.5, 10.0, 4.0, 6.5] será impresso: 
# Média: 6.1
# Valor mais próximo: 6.5

# 1º Passo: Lê o vetor de 5 elementos 

from numpy import append

vetor = []

for i in range (5):                  # O range passa 5 vezes para realizar a adição dos 5 nº
    valor = float(input("Digite o valor: "))
    vetor.append(valor)

# 2º Passo: Calcular a média 

soma = 0
for i in range(5):
    soma = soma + vetor[i]
media = soma / 5

# 3º Passo: Percorrer o vetor e encontrar o valor mais próximo da média

proximo_media = vetor[0]

for elemento in vetor:
    if abs(elemento - media) < abs(proximo_media - media):
        proximo_media = elemento

print("Média:", media)
print("Valor mais próximo da média:", proximo_media) 

