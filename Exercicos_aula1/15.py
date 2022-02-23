# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 15- Dado o valor em quilômetros, converta esse valor em metros

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - -  De Km para metros  - - - - - - - - ###")
print("###########################################################")
print()
km = float(input("Digite o valor quilômetros: "))

# - - - - - Processing - - - - - 
m = km * 1000

# - - - - - - Output - - - - - - 
print("A distância equivalente em metros é de %.2f metros" %(m))
os.system("pause")