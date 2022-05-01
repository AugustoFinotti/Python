# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 19- Faca um programa para verificar se um determinado numero inteiro
# e divisıvel por 3 ou 5, mas nao simultaneamente pelos dois.

# Input
n = int(input("Digite um número: "))
# Processing and Output
if(n%3 == 0):
    print("O número é divisível por 3!")
if(n%5 == 0):
    print("O número é divisível por 5!")
else:
    print("O número não é divisível por 3 e nem por 5!")
