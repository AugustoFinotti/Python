# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# O volume de um cilindro circular e calculado por meio da seguinte fórmula:
# V = π ∗ raio2 ∗ altura (onde π = 3.141592).

# Input
print("############## Área de um Cilindro ##############")
print()
r = float(input("Digite o valor do raio do círculo do cilindro: "))
h = float(input("Digite o valor da altura do cilindro: "))

# Processing
pi = 3.141592
V = (pow(r,2) * pi) * h

# Possíveis soluções
# V = (r**2 * pi ) *h

# Output
print("O Volume do cilindro com as medidas citadas é %.2f" %(V))