# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 34- Leia o valor do raio de um círculo e calcule e imprima
# a area do círculo correspondente. A area do círculo é π ∗ raio2
# considere π = 3.141592.


# Input
print("############## De Raio para Área do círculo ##############")
print()
r = float(input("Digite o valor do raio de um círculo: "))

# Processing
pi = 3.141592
a = ((r * r) * pi) 

# a = (r**2) * pi
# a = pow(r,2) * pi

# Output
print("A área do círculo de raio %.2f será de %.2f" %(r, a))