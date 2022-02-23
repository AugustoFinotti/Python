# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 17- Calcule o volume de uma esfera. (fórmula: V = (4 * pi * r **3 ) /3 )

# Libraries
import os
import math

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - - Volume de uma Esfera - - - - - - - - ###")
print("###########################################################")
print()
r = float(input("Digite o valor do raio: "))

# - - - - - Processing - - - - - 
pi = math.pi
v = (4 * pi * pow(r,3) /3)

# - - - - - - Output - - - - - - 
print("O volume da esfera com esse raio é de %.2f" %(v))
os.system("pause")