# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 02/05/2022

# 8- Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.

maior, menor, i = 0, 0, 1

while(i<=10):
    n = float(input("Digite um número inteiro: "))
    if(n == 1):
        maior = n
        menor = n
    if(n>maior):
        maior = n
    elif(n<menor):
        menor = n
    i +=1
print("O maior valor lido foi: %.2f" %(maior))
print("E o menor valor lido foi: %.2f" %(menor))