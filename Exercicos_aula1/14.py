# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# 14- Calcule a área e o perímetro de um quadrado. (fórmulas: area = lado * lado e perímetro = 4 * lado).

# Bibliotecas
import os

print()
print("###########################################################")
print("### - - - - - Perímetro e área de um quadrado - - - - - ###")
print("###########################################################")
print()

# Entrada
l = float(input("Digite o valor do lado do quadrado: "))

# Processamento
a = l * l
p = l * 4

# Saída
print("A área do quadrado é de %.2f e o perímetro é de %.2f" %(a,p))
os.system("pause")


