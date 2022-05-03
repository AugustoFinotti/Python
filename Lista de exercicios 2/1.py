# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 29 - Faca um programa que receba dois numeros e mostre qual deles eh o maior. 

# Input
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

# Processing and Output
if(num1 > num2):
    print("O maior número é: %.2f" %(num1))
else:
    print("O maior número é: %.2f" %(num2))