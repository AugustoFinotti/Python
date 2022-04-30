# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 6- Escreva um programa que, dados dois numeros inteiros,
# mostre na tela o maior deles, assim como a diferenca existente entre ambos.

# Input
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
# Processing and Output
if(num1 > num2):
    maior = num1
    menor = num2
    print("O primeiro número é maior!")
elif(num2 > num1):
    maior = num2
    menor = num1
    print("O segundo número é maior!")
else:
    maior = num1
    menor = num2
    print("Os número são iguais!")

dif = maior - menor
print("A diferença entre eles é de: %d" %(dif))