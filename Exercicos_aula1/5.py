# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 5- Calcule a área e o perímetro de um quadrado.
# (fórmulas : área = lado*lado e perímetro = 4*lado).

# Entrada
l = float(input("Digite o lado do quadrado: "))

# Processamento
a = l*l
p = l*4

# Saída
print("A área desse quadrado é de %.2f, o perímetro é de %.2f" %(a,l))
os.system("pause")
