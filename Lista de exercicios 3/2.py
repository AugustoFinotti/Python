# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 1- Faca um programa que determine o mostre os cinco primeiros multiplos de 3
# considerando numeros maiores que 0.

print("Exibindo os 5 primeiros números múltiplos de 3")
num = 0
mult = 1
while( mult <= 5 ):
    if(num%3 == 0) and (num != 0):
        print(num)
        mult += 1
    num += 1