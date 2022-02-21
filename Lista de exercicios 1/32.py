# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 32- Leia um numero inteiro e imprima a soma do sucessor de seu triplo
# com o antecessor de seu dobro.

# Input
print("############## Calculador ##############")
print()
num = float(input("Digite um número inteiro: "))

# Processing
calc = ((num * 3) + 1) + ((num * 2) -1)

# ex.: (( 5  * 3) + 1) + (( 5  * 2) -1)  
# ex.: (15 + 1) + (10 - 1)
# ex.: 16 + 9 = 25 

# Output
print("A soma do sucessor do triplo com o antecessor do dobro desse número é:", calc)