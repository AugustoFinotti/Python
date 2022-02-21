# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 21/02/2022

# 52- Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido 
# proporcionalmente ao valor que cada um deu para a realização da aposta.
# Faça um programa que leia quanto cada apostador investiu, o valor do prêmio,
# e imprima quanto cada um ganharia do premio com base no valor investido.

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("## - - - - - - Dividindo o prêmio da Loteria - - - - - - ##")
print("###########################################################")
print()
premio_total = float(input("Digite o valor do prêmio: "))
ap1 = float(input("Digite quanto o primeiro amigo apostou: "))
ap2 = float(input("Digite quanto o segundo amigo apostou: "))
ap3 = float(input("Digite quanto o terceiro amigo apostou: "))
print()

# - - - - - Processing - - - - - 

# aposta total
ap_total = ap1 + ap2 + ap3

# calculando proporcionalmente
premio1 = (premio_total * ap1)/ap_total
premio2 = (premio_total * ap2)/ap_total
premio3 = (premio_total * ap3)/ap_total

# - - - - - - Output - - - - - - 
print("Considerando tais quantias apostadas e calculando proporcionalmente...")
print()
print("O primeiro amigo ganharia: R$ %.2f " %(premio1))
print("O segundo amigo ganharia: R$ %.2f " %(premio2))
print("O terceiro amigo ganharia: R$ %.2f " %(premio3))