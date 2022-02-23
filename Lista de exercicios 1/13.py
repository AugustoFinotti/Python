# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 13. Leia uma distancia em quilometros e apresente-a convertida em milhas.
# A formula de conversão é: M = K / 1,61 , sendo K a distancia em quilometros
# e M em milhas.

# Bibliotecas
import os

# Input
print("############## Conversor de Km para Milhas ##############")
print()
K = float(input("Digite a distância em quilômetros: "))

# Processing
M = K/1.61

# Output
print("A distância equivalente em Milhas é de: %.2f Milhas" %(M))
os.system("pause")