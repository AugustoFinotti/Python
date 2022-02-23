# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 19- Leia um valor de volume em litros e apresente-o convertido em metros cubicos ´ m3.
# A formula de convers ´ ao˜ e: ´ M = L * 1000 , sendo L o volume em litros
# e M o volume em metros cubicos. 

# Bibliotecas
import os

# Input
print("############## Conversor de litros para metros cúbicos ##############")
print()
L = float(input("Digite o valor em Litros: "))

# Processing
M = L / 1000

# Output
print("O valor equivalente em metros cúbicos será de: %.2f m3 " %(M))
os.system("pause")