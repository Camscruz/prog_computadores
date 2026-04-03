# Nome: Camille Cardoso Cruz - Turma: J1
# Tarefa prática 1

# Para usar a biblioteca math encontrada no código é necessário primeiro realizar um comando para chamá-la

import math

# 1)
a = 426027005
b = 200000000
c = 10

k = (str(round((max(math.ceil(a/b), int(b/a), math.sin(a)*b/(a*math.cos(b)+1))) / c * 10 % 3 / c +
               math.log(a, 10)/math.log(b), 4)))

print(f"O valor de K é: {k}")

# 2)
a = 200000000
b = 426027005
c = 20

k = (str(round((max(math.ceil(a/b), int(b/a), math.sin(a)*b/(a*math.cos(b)+1))) / c * 10 % 3 / c +
               math.log(a, 10)/math.log(b), 4)))

print(f"O valor de K é: {k}")

# 3)
a = 500000000
b = 200000000
c = 5

k = (str(round((max(math.ceil(a/b), int(b/a), math.sin(a)*b/(a*math.cos(b)+1))) / c * 10 % 3 / c +
               math.log(a, 10)/math.log(b), 4)))

print(f"O valor de K é: {k}")


# Além disso poderia ser utilizado o input para realizar a escolha em tempo real pelo usuário dos valores de a, b e c

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

k = (str(round((max(math.ceil(a/b), int(b/a), math.sin(a)*b/(a*math.cos(b)+1))) / c * 10 % 3 / c +
               math.log(a, 10)/math.log(b), 4)))

print(f"O valor de K é: {k}")
