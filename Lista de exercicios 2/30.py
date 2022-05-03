# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 30 - Faca um programa que receba tres numeros e mostre-os em ordem crescente.

# tabela de possibilidades de entrada
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 2 1
# 3 1 2

# Input
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
# Processing and Output
if(n1<=n2) and (n2<=n3):                 # 1 2 3
    s1, s2, s3 = n1, n2, n3         # definindo várias variáveis em uma linha só, respectivamente

elif(n1<=n2) and (n2>=n3) and (n1<=n3):  # 1 3 2
    s1, s2, s3 = n1, n3, n2

elif(n1>=n2) and (n2<=n3) and (n1<=n3):  # 2 1 3
    s1, s2, s3 = n2, n1, n3

elif(n1<=n2) and (n2>=n3) and (n3<=n1):  # 2 3 1
    s1, s2, s3 = n3, n1, n2

elif(n1>=n2) and (n2>=n3):               # 3 2 1
    s1, s2, s3 = n3, n2, n1

elif(n1>=n2) and (n2<=n3) and (n3<=n1):  # 3 1 2
    s1, s2, s3 = n2, n3, n1

print(s1, s2, s3)