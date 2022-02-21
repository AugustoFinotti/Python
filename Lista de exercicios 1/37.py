# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 37- Faça um programa que leia o valor de um produto e imprima o valor com desconto
# tendo em vista que o desconto foi de 12%

# Input
print("############## Desconto de 12% ##############")
print()
p1 = float(input("Digite o preço total do produto: "))

# Processing
d = 1 - 0.12
p2 = p1 * d

# Output
print("Com 12 por cento de desocnto o preço final será de %.2f $" %(p2))