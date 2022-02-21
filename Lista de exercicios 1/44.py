# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 44- Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar 
# subindo a escada. Calcule e mostre quantos degraus o usuario deverá
# subir para atingir seu objetivo.

# libraries
import math

# Input
print("############## Altura por Degraus ##############")
print()
h = float(input("Digite qual é a altura que você deseja alcançar: "))
h_d = float(input("Digite qual será a altura de cada degrau: "))

# Processing
dgrs = math.ceil(h / h_d)

# Output
print("Então é necessário %.2f degraus para alnçar essa altura" %(dgrs))
