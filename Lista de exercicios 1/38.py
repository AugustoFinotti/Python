# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 38- Leia o salario de um funcionário. Calcule e imprima o valor do
# novo salário, sabendo que ele recebeu um aumento de 25%.

# Bibliotecas
import os

# Input
print("############## Aumento de 25% ##############")
print()
s1 = float(input("Digite o valor do salário atual: "))

# Processing
s2 = s1 * 1.25

# Output
print("Depois de um aumento de 25 por cento o novo salário será de %.2f $" %(s2))
os.system("pause")