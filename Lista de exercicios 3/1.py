# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 25/05/2022

# 1- Faca um programa que determine e mostre os cinco primeiros multiplos de 3
# considerando numeros maiores que 0.
# (3, 6, 9, 12 e 15)

# - - - Solução com WHILE

# print("Exibindo os 5 primeiros números múltiplos de 3")
# num = 0
# mult = 1
# while( mult <= 5 ):
#     if(num%3 == 0) and (num != 0):
#         print(num)
#         mult += 1
#     num += 1

# - - - Solução com FOR

for n in range (3, 16, 3): # de 1 a 15 de 3 em 3
    print(n)