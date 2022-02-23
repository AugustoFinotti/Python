# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 15. Leia um angulo em radianos e apresente-o convertido em graus.
# A formula de conversão é: G = R ∗ 180/π, sendo G o angulo em graus
# e R em radianos e π = 3.14.

# Bibliotecas
import os

# Importing Libraries
import math

# Input
print("############## Conversor de Radianos para Graus  ##############")
print()
R = float(input("Digite o valor do ângulo em Radianos: "))
pi = math.pi

# Processing
G = R * 180/pi

# Output
print("O valor equivalente em Graus é de: %.2f º" %(G))
os.system("pause")