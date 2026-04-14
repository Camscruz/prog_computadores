# Nome: Camille Cardoso Cruz - Turma: J1
# Aula prática 03

# Escreva um programa que leia um número inteiro e imprima o seu nº de dígitos correspondente

a = int(input("Informe um número inteiro: "))
k = 0

while (a > 0):
    a = a//10
    k = k+1

print("O número de dígitos de a é:" + str(k))
