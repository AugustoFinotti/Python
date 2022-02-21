# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 47- Leia um número inteiro de 4 dígitos (de 1000 a 9999)
# e imprima 1 dígito por linha.

# Input
print("############## Leitor de Algarismos ##############")
print()
num = int(input("Digite um número inteiro de 4 algarismos: "))

# Processing
alg1 = int(num // 1000)
alg2 = int((num - (alg1 * 1000)) // 100)
alg3 = int((num - (alg1 * 1000 + (alg2 * 100))) // 10)
alg4 = int(num - (alg1 * 1000) - (alg2 * 100) - (alg3 * 10))

# Output
print(alg1)
print(alg2)
print(alg3)
print(alg4)