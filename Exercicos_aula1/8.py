# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 8- Calcule o valor do resto e do quociente da divisão de dois números inteiros.

# Entrada
n1 = float(input("Digite o valor do primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))

# Processamento
res = n1 % n2
quo = n1 / n2

# Saída
print("Em uma divisão com o primeiro número pelo segundo número, o quociente é %.2f e o resto é %.2f" %(quo, res))
os.system("pause")
