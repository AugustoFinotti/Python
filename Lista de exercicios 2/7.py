# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 7- Faca um programa que receba dois numeros e mostre o maior.
# Se por acaso, os dois numeros forem iguais, imprima a mensagem "Numeros iguais".

# Input
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
# Processing and Output
if(num1 > num2):
    print("O primeiro número é o maior!")
elif(num2 > num1):
    print("O segundo número é o maior!")
else:
    print("Números iguais!")
