# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 10-  Faca um programa que receba a altura e o sexo de uma pessoa e calcule
# e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde a altura):
# • Homens: (72.7 ∗ h) − 58
# • Mulheres: (62, 1 ∗ h) − 44, 7

# Input
h = float(input("Digite sua altura em metros: "))
sexo = input("Digite o seu sexo (feminino ou masculino): ")
# Processing and Output
if(sexo == "feminino"):
    peso_ideal = (72.7 * h) - 58
    print("Seu peso ideal é de: %.2f" %(peso_ideal))
else:
    peso_ideal = (62.1 * h) - 44.7
    print("Seu peso ideal é de: %.2f" %(peso_ideal))
