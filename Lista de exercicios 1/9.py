# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 9- Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
# A formula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
# temperatura em Kelvin.

# Input
print("############## Conversor de Celsius para Kelvin ##############")
print()
C = float(input("Digite a temperatura em Celsius: "))

# Processing
K = C + 273.15

# Output
print("Essa temperatura em Kelvin será de %.2f K" %K)
