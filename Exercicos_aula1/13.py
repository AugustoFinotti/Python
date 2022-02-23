# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 13- Calcular o valor do Perímetro
# ( 2*comprimento + 2*largura ) de um retângulo.

# Entrada
print("Vamos calcular o perímetro de um retângulo")
comprimento = float(input("Digite o valor do comprimento do retângulo: "))
largura = float(input("Digite o valor da largura do retângulo: "))

# Processamento
perimetro = (2*comprimento + 2*largura)

# Saída
print("O perímetro do retângulo é de %.2f" %(perimetro))
os.system("pause")
