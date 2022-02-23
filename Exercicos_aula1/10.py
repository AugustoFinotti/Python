# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 10- Calcular o valor de uma viagem de uma cidade a outra.

# Entrada
print("Calcular o custo de uma viagem de uma cidade a outra")
d = float(input("Digite em km a distância: "))
vl = float(input("Digite o preço do litro do combustível: "))
des = float(input("Digite quatos litros o carro gasta por km: "))
pedagio = float(input("Digite o custo do pedágio: "))

# Processamento
custo_total = ((d * vl) / des ) + pedagio

# Saída
print("O custo total da viagem será de: %.2f" %(custo_total))
os.system("pause")
