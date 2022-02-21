# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 27- Leia um valor de area em hectares e apresente-o convertido em metros quadrados m2.
# A formula de conversão é: M = H * 10000, sendo M a area em metros quadrados
# e H a area em hectares.

# Input
print("############## Conversor de Hectare para Metros Quadrados ##############")
print()
H = float(input("Digite o valor da área em Hectares: "))

# Processing
M = H * 10000

# Output
print("O valor da área é equivalente a %.2f Metros Quadrados" %(M))
