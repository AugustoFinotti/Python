# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 45- Faça um programa para converter uma letra maiuscula em letra minúscula.
# Use a tabela ASCII para resolver o problema.

# Bibliotecas
import os

# Input
print("############## Maiúscula para Minúscula ##############")
print()
c = input("Digite um letra Maiúscula: ")

# Processing
c = c.lower()

# Output
print("A letra digitada na forma Minúscula é: %s" %(c))
os.system("pause")