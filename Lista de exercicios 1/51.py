# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 19/02/2022

# 51- Escreva um programa que leia as coordenadas x e y
# de pontos no R2 e calcule sua distância da origem (0, 0).

# Bibliotecas
import os

# Input
print("############## Distância do ponto da origem ##############")
print()
print("Vamos calcular a distância da origem até um determinado ponto...")
print()
x = int(input("Digite o valor da coordenada X: "))
y = int(input("Digite o valor da coordenada Y: "))

# Processing
d = float(pow(pow(x,2) + pow(y,2), 0.5))

# Output
print("A distância entre a origem e o ponto é de: %.2f" %(d))
os.system("pause")