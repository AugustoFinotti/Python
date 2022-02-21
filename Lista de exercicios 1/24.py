# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 24- Leia um valor de area em metros quadrados m2 e apresente-o convertido em acres.
# A formula de conversão é A = M * 0.000247, sendo M a area em metros quadrados
# e A a area em acres

# Input
print("############## Conversor de Metros Quadrados para Acres ##############")
print()
M = float(input("Digite o valor da área em Metros Quadrados: "))

# Processing
A = M * 0.000247

# Output
print("O valor da área equivale a %.2f Acres"%(A))
