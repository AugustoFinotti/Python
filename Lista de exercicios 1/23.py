# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 23- Leia um valor de comprimento em metros e apresente-o convertido em jardas.
# A formula de conversão é: J = M / 0.91 , sendo J o comprimento em jardas
# e M o comprimento em metros.

# Input
print("############## Conversor de Metros para Jardas ##############")
print()
M = float(input("Digite o valor da distância em Metros: "))

# Processing
J = M / 0.91

# Output
print("Essa distância equivale a %.2f Jardas"%(J))
