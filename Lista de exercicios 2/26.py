# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 26 - Leia a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
# calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
#    CONSUMO     (Km/l)     MENSAGEM
#    menor que     8      Venda o carro!
#    entre       8 e 12     Economico!
#    maior que     14    Super economico! 

# Input
km = float(input("Digite  distância percorrida em Km pelo carro: "))
l = float(input("Digite a quantidade de litros consumidos nesse percurso: "))
cons = km/l
if(cons<8):
    print("Venda o carro!")
elif(cons >= 8) and ( cons <= 12):
    print("Econômico!")
elif(cons > 14):
    print("Super econômico!")