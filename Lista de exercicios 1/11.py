# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 11- Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
# (quilometros por hora). A fórmula de conversão é: ´ K = M ∗ 3.6, sendo K a velocidade
# em km/h e M em m/s.

# Bibliotecas
import os

# Input
print("############## Conversor de m/s para km/h ##############")
print()
M = float(input("Digite a velocidade em metros por segundo: "))

# Processing
K = M*3.6

# Output
print("A velocidade equivalente em km/h é a de: %.2f km/h" %(K))
os .system("pause")