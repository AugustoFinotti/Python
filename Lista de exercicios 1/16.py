# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 16- Leia um valor de comprimento em polegadas e apresente-o convertido em cent´ımetros.
# A formula de conversão é: C = P * 2.54 , sendo C o comprimento em centımetros
# e P o comprimento em polegadas.

# Bibliotecas
import os

# Input
print("############## Conversor de polegadas para centímetros  ##############")
print()
P = float(input("Digite o valor da distância em polegadas: "))

# Processing
C = P * 2.54

# Output
print("O valor equivalente em centímetros é de %.2f cm" %(C))
os.system("pause")