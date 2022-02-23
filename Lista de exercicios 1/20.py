# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 20- Leia um valor de massa em quilogramas e apresente-o convertido em libras.
# A formula de conversão é: L = K 0.45 , sendo K a massa em quilogramas
# e L a massa em libras

# Bibliotecas
import os

# Input
print("############## Coversor de Kg para Libras ##############")
print()
K = float(input("Digite o valor da massa em quilogramas: "))

# Processing
L = K / 0.45

# Output
print("A massa equivalente é de: %.2f Libras" %(L))
os.system("pause")