# Nome: Camille Cardoso Cruz - Turma: J1
# Tarefa prática 2

# A expressão dada é:
# t = x % y < z // x or x * y / 9 > z + x and z * y < x * w
# Para x = 426027005; y = 7; z = 600000000; w = 17;
# Para x = 426027005; y = 13; z = 500000000; w = 19;
# Para x = 426027005; y = 16; z = 700000000; w = 12;

#Para usar a biblioteca math encontrada no código é necessário primeiro realizar um comando para chamá-la

# 1)
x, y, z, w = 426027005, 7, 600000000, 17

t = x % y < z // x or x * y / 9 > z + x and z * y < x * w

print(f"O valor de t é: {t}")

# 2)
x, y, z, w = 426027005, 13, 500000000, 19

t = x % y < z // x or x * y / 9 > z + x and z * y < x * w

print(f"O valor de t é: {t}")

# 3)
x, y, z, w = 426027005, 16, 700000000, 12

t = x % y < z // x or x * y / 9 > z + x and z * y < x * w

print(f"O valor de t é: {t}")