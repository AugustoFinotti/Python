# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 5- Faca um programa que peca ao usuario para digitar 10 valores e some-os

soma = 0
for x in range(1, 11):
    valor = float(input("Digite um valor: "))
    soma = soma + valor
print("A soma dos valores resultou em: %.2f" %(soma))