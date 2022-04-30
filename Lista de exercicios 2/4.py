# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 4- Faca um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
# • O numero digitado ao quadrado
# • A raiz quadrada do numero digitado

# Input
num = int(input("Digite um número: "))
# Processing and Output
if(num>0):
    raiz = pow(num, 0.5)
    quad = num ** 2
    print("Esse número ao quadrado resulta em: %.2f, e a raiz quadrada desse número é: %.2f." %(quad, raiz))
else:
    print("fim do programa")