# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 33- Leia o tamanho do lado de um quadrado
# e imprima como resultado a sua area.

# Bibliotecas
import os

# Input
print("############## Área de um quadrado ##############")
print()
l = float(input("Digite o valor do lado do quadrado: "))

# Processing
a = l * l
# a = l**2
# a = pow(l,2) 

# Output
print("A área de um quadrado com lado %.2f, será de %.2f" %(l, a))
os.system("pause")