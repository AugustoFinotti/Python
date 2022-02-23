# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A formula de conversão é: C = K − 273.15, sendo C a temperatura em Celsius e K a
# temperatura em Kelvin.

# Bibliotecas
import os

# Input
print("############## Conversor de Kelvin para Celsius ##############")
print()
K = float(input("Digite a temperatura em Kelvin: "))

# Processing
C = K -273.15

# Output
print("A temperatura equivalente em Celsius é: %.2f Cº" %(C))
os.system("pause")