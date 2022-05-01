# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 6- Faca um programa que leia 10 inteiros e imprima sua media.

i = 1
soma = 0
while( i <= 10 ):
    valor = int(input("Digite um valor inteiro: "))
    soma = soma + valor
    i += 1
media = soma / (i -1)
print("A média dos valores resultou em: %.2f" %(media))