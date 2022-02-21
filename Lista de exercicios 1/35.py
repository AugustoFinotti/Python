# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 35. Sejam a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação:
# hipotenusa = √ a2 + b2. Faça um programa que receba os valores de a e b
# e calcule o valor da hipotenusa atraves da equação.
# Imprima o resultado dessa operação. 

# Input
print("############## Calculadora de Hipotenusa ##############")
print()
a = float(input("Digite o cateto A do triângulo: "))
b = float(input("Digite o cateto B do triângulo: "))

# Processing
h = pow( (pow(a,2)) + (pow(b,2)), 0.5 )

# Possíveis soluções
# h = pow( (a**2 + b**2), 0.5 )
# h = (a**2 + b**2) **0.5

# s_q = pow(a,2) + pow(b,2) 
# h = pow(s_q,0.5)

# Output
print("A Hipotenusa desse triângulo tem o valor de %.2f" %(h))
