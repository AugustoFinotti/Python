# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 22- Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#   a)	O novo peso, se a pessoa engordar 15% sobre o peso digitado;
#   b)	O novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - - Calculadora de Peso - - - - - - - - ###")
print("###########################################################")
print()
peso_a = float(input("Digite o seu peso atual em kg: "))

# - - - - - Processing - - - - - 
p_mais_15 = peso_a * 1.15
p_menos_20 = peso_a * 0.8

# - - - - - - Output - - - - - - 
print("Você teria %.2f Kg engordando 15 por cento e teria %.2f Kg emagrecendo 20 por cento do seu peso" %(p_mais_15, p_menos_20))
os.system("pause")