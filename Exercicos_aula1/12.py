# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 12- Calcular o valor de x1 e x2 em uma equação do 2º grau
# (considere que o valor de delta é positivo).

# Entrada
print("Vamos achar x1 w x2 através da fórmula de bhaskara")
A = float(input("Digite o valor do A na equação: "))
B = float(input("Digite o valor dO B na equação: "))
C = float(input("Digite o valor de C na equação: "))

# Processamento
delta = pow(B,2) - 4*A*C
x1 = (-B + pow(delta,0.5))/ (2*A)
x2 = (-B - pow(delta,0.5))/ (2*A)

# Saída
print("x1 é %.2f e x2 é %.2f" %(x1,x2))
os.system("pause")
