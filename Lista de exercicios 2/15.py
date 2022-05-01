# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 15- Usando if, elif e else, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
# da semana correspondente a este numero. Isto e, domingo se 1, segunda-feira se 2, e
# assim por diante.

# Input
n = float(input("Digite um número inteiro de 1 a 7: "))
# Processing and Output
if(n == 1):
    print("Domingo")
elif(n == 2):
    print("Segunda-feira")
elif(n ==3):
    print("Terça-feira")
elif(n ==4):
    print("Quarta-feita")
elif(n ==5):
    print("Quinta-feita")
elif(n ==6):
    print("Sexta-feita")
elif(n ==7):
    print("Sábado")
else:
    print("Número inválido!")