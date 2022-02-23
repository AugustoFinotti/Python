# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os
import math

# 5- Calcule o volume de uma esfera. (fórmula: V = 4 pi r 3 )
#                                                      3 

# Entrada
r = float(input("Digite o valor do raio do círculo: "))

# Processamento
pi = math.pi
V = (4.0 * pi * pow(r,3))/3.0

# Saída
print("O valor do volume dessa esfera é de %.2f" %(V))
os.system("pause")
