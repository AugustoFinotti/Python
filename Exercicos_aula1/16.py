# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 16- Uma empresa paga o salário bruto dos funcionários e deduz 5% de imposto.
# Qual o salário líquido e o valor do desconto para cada funcionário.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - -  Salário com imposto descontado  - - - - - ###")
print("###########################################################")
print()
sal_b = float(input("Digite o salário do fncionário: "))

# - - - - - Processing - - - - - 
imp = sal_b * 0.05
sal_l = sal_b - imp 

# - - - - - - Output - - - - - - 
print("O desconto para o imposto foi de %.2f e o salário líquido é de %.2f" %(imp,sal_l))
os.system("pause")