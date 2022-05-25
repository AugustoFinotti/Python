# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 25/05/2022

# 2- Escreva um programa que escreva na tela, de 1 ate 100, de 1 em 1, 2 vezes.
# A primeira vez deve usar a estrutura de repetic¸ao˜ for,
# a segunda while.

# bibliotecas
import time

# - - FOR
for x in range (1, 101):
    print(x)
    time.sleep(0.1)
x = 1

# - - WHILE
x = 1
while( x <= 100 ):
    print(x)
    time.sleep(0.1)
    x += 1 # x = x + 1