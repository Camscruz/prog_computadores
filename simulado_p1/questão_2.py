n = int(input())
j = n//3
i = 0
k = 0

while i < j:
    for t in range(1, n, 2):
        k = k+1
    i = i+1

print(i, k)
