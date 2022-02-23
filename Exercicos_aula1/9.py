# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 9- Calcule a raiz quadrada e raiz cúbica de um determinado número.

# Entrada
n = float(input("Digite um número qualquer: "))

# Processamento
r2 = pow(n,0.5)
r3 = pow (n,0.33333)

# Saída
print("A raíz quadrada será de %.2f e a raiz cúbica será de %.2f" %(r2,r3))
os.system("pause")
