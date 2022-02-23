# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 19 - Calcule a raiz quadrada e raiz cúbica de um determinado número.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - -  Raiz quadrada e cúbica  - - - - - - - ###")
print("###########################################################")
print()
n = float(input("Digite um número: "))

# - - - - - Processing - - - - - 
r2 = pow(n,1/2)
r3 = pow(n,1/3)

# - - - - - - Output - - - - - - 
print("A raiz quadrada desse número é %.2f e a raiz cúbica é %.2f" %(r2,r3))
os.system("pause")