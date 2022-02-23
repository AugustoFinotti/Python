# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 11- Calcular os juros simples de uma aplicação financeira.
# Juros = capital * taxa/100 *periodo

# Entrada
print("Vamos realizar uma aplicação financeira")
cap = float(input("Digite o valor do capital investido: "))
taxa = float(input("Digite a taxa de rendimento mensal dessa aplicação: "))
per = float(input("Por quantos meses o capital será investido: "))

# Processamento
juros = cap * taxa/100 * per

# Saída
print("Os juros dessa aplicação renderão R$ %.2f" %(juros))
os.system("pause")
