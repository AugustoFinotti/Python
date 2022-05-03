# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
#           Categoria      Idade
#           Infantil A     5 a 7
#           Infantil B     8 a 10
#           Juvenil A      11 a 13
#           Juvenil B      14 a 17
#           Senior         maiores de 18 anos

# Input
idade = int(input("Digite a idade de um nadador: "))
# Processing and Output
if(idade>=5) and (idade<=7): # Infantil A - 5 a 7
    print("Categoria Infantil A")

elif(idade>=8) and (idade<=10): # Infantil B - 8 a 10
    print("Categoria Infantil B")

elif(idade>=11) and (idade<=13): # Juvenil A - 11 a 13
    print("Categoria Juvenil A")

elif(idade>=14) and (idade<=17): # Juvenil B - 14 a 17
    print("Categoria Juvenil B")

elif(idade>=18): # Senior - maiores de 18 anos
    print("Categoria Sênior")