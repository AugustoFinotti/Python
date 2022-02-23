# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 24- Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário
# calcule e mostre a quantidade de salários que esse funcionário ganha.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - -  Salário em Salário Mínimo  - - - - - - ###")
print("###########################################################")
print()
sal_m = float(input("Digite o valor de um salário mínimo: "))
sal_t = float(input("Digite o valor do salário de um funcionário: "))

# - - - - - Processing - - - - - 
sal_f = sal_t / sal_m 

# - - - - - - Output - - - - - - 
print("Esse funcionário recebe o equivalente a %.1f salário(s) mínimo(s) " %(sal_f))
os.system("pause")

