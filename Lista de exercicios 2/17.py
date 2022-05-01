# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 17- Faca um programa que calcule e mostre a area de um trapezio. Sabe-se que:
# A = (basemaior + basemenor) ∗ altura
#                2
# Lembre-se a base maior e a base menor devem ser numeros maiores que zero. 

# Input
print("Vamos calcular a área de um trapézio: ")
bma = float(input("Digite o valor da base maior: "))
bme = float(input("Digite o valor da base menor: "))
h = float(input("Digite o valor da altura: "))
# Processing and Output
if(bma>0) and (bme>0) and (h>0):
    area = ((bma + bme) * h) /2
    print("A áre desse trapézio é de: %.2f" %(area))
else:
    print("Valores inválidos!")