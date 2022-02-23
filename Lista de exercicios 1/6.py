# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 6- Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A formula de conversao é: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Bibliotecas
import os

# Input
print("############ Conversor de Graus Celsius para Fahrenheit ############")
print ()
C = float(input("Digite a temperatura em Graus Celsius: "))

# Processing
F = C*(9.0/5.0)+32.0

# Output
print("A temperatura equivalente em Fahrenheit é: %.2f" %(F))
os.system("pause")