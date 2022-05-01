# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 23- Determine se um determinado ano lido e bissexto. Sendo que um ano e bissexto se
# for divisıvel por 400 ou se for divisıvel por 4 e nao for divisıvel por 100.
# Por exemplo: 1988, 1992, 1996

# Input
ano = int(input("Digite um determinado ano: "))
# Processing and Output
if(ano%400 == 0) or ((ano%4 == 0) and (not (4%100 == 0))):
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")