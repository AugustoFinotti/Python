# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 14- Leia um angulo em graus e apresente-o convertido em radianos.
# A formula de conversão é: R = G ∗ π/180, sendo G o angulo em graus
# e R em radianos e π = 3.14.

# Importing Libraries
import math

# Input
print("############## Conversor de Graus para Radianos ##############")
print()
G = float(input("Digite o valor do ângulo em Graus: "))
pi = math.pi

# Processing
R = G * pi/180

# Output
print("O valor equivalente em Radianos é de: %.2f rad" %(R))
