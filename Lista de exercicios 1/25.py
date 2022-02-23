# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 25- Leia um valor de area em acres e apresente-o convertido em metros quadrados m2.
# A formula de conversão é: M = A * 4048.58, sendo M a area em metros quadrados
# e A a area em acres.

# Bibliotecas
import os

# Input
print("############## Conversor de Acres para Metros Quadrados ##############")
print()
A = float(input("Digite o valor da área em Acres: "))

# Processing
M = A * 4048.58

# Output
print("O valor da área equivale a %.2f Metros Quadrados"%(M))
os.system("pause")