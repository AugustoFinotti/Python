# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 23- Faça um programa que calcule e mostre a área de um losango. Sabendo-se que 
# Area = (diagonal maior * diagonal menor) / 2


# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - -  Área de um Losango - - - - - - - - ###")
print("###########################################################")
print()
d_me = float(input("Digite o valor da diogonal maior: "))
d_ma = float(input("Digite o valor da diagonal menor: "))

# - - - - - Processing - - - - - 
a = (d_me * d_ma) /2

# - - - - - - Output - - - - - - 
print("A área de losango é de %.2f" %(a))
os.system("pause")