# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 20- Leia os valores dos catetos de um triângulo e exiba a hipotenusa (hipotenusa2 = cateto12 + cateto22)

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - - - - Hipotenusa  - - - - - - - - - - ###")
print("###########################################################")
print()
cat1 = float(input("Digite o valor do cateto 1: "))
cat2 = float(input("Digite o valor do cateto 2: "))

# - - - - - Processing - - - - - 
hip = pow( pow(cat1,2) + pow(cat2,2) , 0.5)

# - - - - - - Output - - - - - - 
print("A Hipotenusa é de %.2f" %(hip))
os.system("pause")