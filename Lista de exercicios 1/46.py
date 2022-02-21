# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 46- Faça um programa que leia um numero inteiro positivo de três dígitos (de 100 a 999).
# Gere outro numero formado pelos dígitos invertidos do numero lido.
# Exemplo: NumeroLido = 123 NumeroGerado = 321.

# Input
print("############## INVERSOR DE ALGARISMOS - 3 dígitos ##############")
print()
num = int(input("Digite um número inteiro formado por 3 algarismos: "))

# Processing
alg1 = int(num//100)
alg2 = int((num - (alg1 * 100)) //10)
alg3 = int(num - ((alg1 * 100) + (alg2 * 10)))

# Output
print ("%d%d%d" %( alg3, alg2, alg1))
