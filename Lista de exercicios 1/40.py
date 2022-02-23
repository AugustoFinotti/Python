# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 40- Uma empresa contrata um encanador a R$ 30,00 por dia.
# Faça um programa que solicite o numero de dias trabalhados pelo encanador
# e imprima a quantia líquida que deverá ser paga
# sabendo-se que sao descontados 8% para imposto de renda.

# Bibliotecas
import os

# Input
print("############## Custo do Encanador ##############")
print()
d = float(input("Digite o número de dias que serão necessários para o serviço: "))

# Processing
p = 30 * d * 0.92

# Output
print("Considerando R$ 30 por dia de custo, %.2f dias de serviço, e 8 por cento de imposto de renda" %(d))
print("O custo final será de R$ %.2f" %(p))
os.system("pause")