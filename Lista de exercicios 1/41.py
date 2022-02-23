# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 41- Faça um programa que leia o valor da hora de trabalho (em reais)
# e número de horas trabalhadas no mes. Imprima o valor a ser pago ao funcionário,
# adicionando 10% sobre o valor calculado.

# Bibliotecas
import os

# Input
print("############## Calculador de Salário ##############")
print()
vh = float(input("Digite o valor por hora de trabalho:  "))
ht = float(input("Digite o número de horas trabalhadas: "))

# Processing
s = vh * ht * 1.1

# Output
print("Adicionando 10 por cento, o valor final do salário desse funcionário será de R$ %.2f " %(s))
os.system("pause")