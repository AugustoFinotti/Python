# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 7- Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A formula de conversao é: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
# e F a temperatura em Fahrenheit.

# Input
print("############ Conversor de Fahrenheit para Graus Celsius ############")
print ()
F = float(input("Digite a temperatura em Graus Fahrenheit: "))

# Processing
C = 5.0*(F-32.0)/9.0

# Output
print("A temperatura equivalente em Graus Celsius é: %.2f Cº" %C)
