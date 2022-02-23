# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 29- Leia quatro notas, calcule a média aritmética e imprima o resultado.

# Bibliotecas
import os

# Input
print("############## Calculadora de notas ##############")
print()
n1 = float(input("Digite sua nota na primeira prova: "))
n2 = float(input("Digite sua nota na segunda prova: "))
n3 = float(input("Digite sua nota na terceira prova: "))
n4 = float(input("Digite sua nota na quarta prova: "))

# Processing
m = (n1 + n2 + n3 + n4)/4

# Output
print("Sua média aritmética das 4 provas é de: %.2f" %(m))
os.system("pause")