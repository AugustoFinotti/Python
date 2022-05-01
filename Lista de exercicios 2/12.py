# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 12- Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem “Numero invalido”.
# Se o numero for positivo, calcular o logaritmo deste numero. 

# Libraires
import math
# Input
num = int(input("Digite um número: "))
# Processing and Output
if(num>0):
    log = math.log(num)
    print("O logaritmo desse número é de: %.2f" %(log))
else:
    print("Número inválido")
