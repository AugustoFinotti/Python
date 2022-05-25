# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 25/05/2022

# 9- Faca um programa que leia um numero inteiro N e depois imprima
# os N primeiros numeros naturais ımpares
# N = 5 -> 1 3 5 7 9

n = int(input("Digite um número inteiro: "))
impar = 1
for x in range(n):
    print(impar)
    impar += 2