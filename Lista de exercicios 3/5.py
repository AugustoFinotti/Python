# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 5- Faca um programa que peca ao usuario para digitar 10 valores e some-os

i = 1
soma = 0
while( i <= 10 ):
    valor = float(input("Digite um valor: "))
    soma = soma + valor
    i += 1
print("A soma dos valores resultou em: %.2f" %(soma))