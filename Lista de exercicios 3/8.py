# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 25/05/2022

# 8- Escreva um programa que leia 10 numeros e escreva o menor valor lido
# e o maior valor lido.

# usando WHILE
# i = 1
# while(i<=10):
#     numero = float(input("Digite um número(%d): " %(i)))
#     if(i==1):
#         maior = numero
#         menor = numero
#     elif(numero > maior):
#         maior = numero
#     elif(numero < menor):
#         menor = numero
#     i += 1
# print("O menor é %.2f e o menor é %.2f" %(menor, maior))

# usando FOR
for i  in range(1,11):
    numero = float(input("Digite um número(%d): " %(i)))
    if(i==1):
        maior = numero
        menor = numero
    elif(numero > maior):
        maior = numero
    elif(numero < menor):
        menor = numero
        
print("O menor é %.2f e o menor é %.2f" %(menor, maior))