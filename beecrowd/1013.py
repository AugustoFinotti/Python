A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

maior = (A + B + abs(A - B))  / 2
resultado = (maior + C + abs(maior - C))/2

print("%d eh o maior" %resultado)