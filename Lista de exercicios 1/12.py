# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 12. Leia uma distancia em milhas e apresente-a convertida em quilometros.
# A fórmula de conversão é: K = 1, 61 ∗ M, sendo K a distancia em quilometros
# e M em milhas.

# Input
print("############## Conversor de Milhas para Km ##############")
print()
M = float(input("Digite a distância em Milhas: "))

# Processing
K = M*1.61

# Output
print("A distância equivalente em quilômetros é de %.2f Km" %(K))
