# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 26- Leia um valor de area em metros quadrados m2 e apresente-o convertido em hectares.
# A formula de conversão é: H = M * 0.0001 sendo M a area em metros quadrados
# e H a area em hectares. 

# Input
print("############## Conversor de Metros Quadrados para Hectare ##############")
print()
M = float(input("Digite o valor da área em Metros Quadrados: "))

# Processing
H = M * 0.0001

# Output
print("O valor da área equivale a %.2f Hectares"%(H))
