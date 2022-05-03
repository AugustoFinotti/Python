# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 31 - Faca um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir,
# verifique e mostra qual a classificacao dessa pessoa
#        Altura    |                        Peso
#                  |   Ate 60  |  Entre 60 e 90 (Inclusive)  |  Acima de 90
# Menor que 1,20   |      A    |               D             |       G
# De 1,20 a 1,70   |      B    |               E             |       H
# Maior que 1,70   |      C    |               F             |       I

# Input
h = float(input("Digite sua altura em metros: "))
p = float(input("Digite seu peso em Kg: "))
# Processing and Output
if(h<1.2):
    if(p<60):
        cat = "A"
    elif(p>=60) and (p<=90):
        cat = "D"
    else:
        cat = "G"
elif(h>=1.2) and (h<=1.7):
    if(p<60):
        cat = "B"
    elif(p>=60) and (p<=90):
        cat = "E"
    else:
        cat = "H"
else:
    if(p<60):
        cat = "C"
    elif(p>=60) and (p<=90):
        cat = "F"
    else:
        cat = "I"
print("Sua catedora é: %s" %(cat))