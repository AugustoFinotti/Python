# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 02/05/2022

# 9- Faca um programa que leia um numero inteiro N
# e depois imprima os N primeiros numeros naturais ımpares.

n = int(input("Digite um número inteiro: "))
n_imp = 0
if(n <= 0):
    n_imp = 1
    n = n *-1
    while(n >= 1):
        print(n_imp)
        n_imp += 2
        n -= 1
elif(n%2==0):
    n_imp = n + 1
    while(n >= 1):
        print(n_imp)
        n_imp += 2
        n -= 1
else:
    while(n >= 1):
        print(n_imp)
        n_imp += 2
        n -= 1