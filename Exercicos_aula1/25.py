# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 25- Faça um programa que receba o ano do nascimento de uma pessoa e o ano atual, calcule e mostre: 
#   a)	A idade da pessoa em anos
#   b)	A idade da pessoa em meses
#   c)	A idade da pessoa em dias

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - - Calculador de Idade - - - - - - - - ###")
print("###########################################################")
print()
ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# - - - - - Processing - - - - - 
id_ano = ano_atual - ano_nasc
id_meses = id_ano * 12
id_dias = id_meses * 30

# - - - - - - Output - - - - - - 
print("Considerando que você fez aniversário esse ano, você tem %d anos ou %d meses ou ainda %d dias" %(id_ano, id_meses, id_dias))
os.system("pause")

