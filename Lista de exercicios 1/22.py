# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 22- Leia um valor de comprimento em jardas e apresente-o convertido em metros.
# A formula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas
# e M o comprimento em metros.

# Bibliotecas
import os

# Input
print("############## Conversor de Jardas para Metros ##############")
print()
J = float(input("Digite o valor da distância em Jardas: "))

# Processing
M = J * 0.91

# Output
print("Essa distância equivale a %.2f Metros"%(M))
os.system("pause")