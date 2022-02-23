# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 21- Leia um valor de massa em libras e apresente-o convertido em quilogramas.
# A formula de conversão é: K = L * 0.45 , sendo K a massa em quilogramas
# e L a massa em libras.

# Bibliotecas
import os

# Input
print("############## Coversor de Libras para Kg ##############")
print()
L = float(input("Digite o valor da massa em Libras: "))

# Processing
K = L * 0.45

# Output
print("O valor equivalente da massa será de %.2f Kg"%(K))
os.system("pause")