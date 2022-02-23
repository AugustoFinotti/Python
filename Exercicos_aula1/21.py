# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 21- Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
# Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas,
# calcule e mostre a comissão e seu salário final.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - Calculadora de Salário  - - - - - - - ###")
print("###########################################################")
print()
sal_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas: "))

# - - - - - Processing - - - - - 
comiss = vendas * 0.04
sal_final = sal_fixo + comiss

# - - - - - - Output - - - - - - 
print("A comissão desse funcinário é de %.2f R$, e seu salário é de %.2f" %(comiss, sal_final))
os.system("pause")