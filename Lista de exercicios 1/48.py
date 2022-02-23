# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 48- Leia um valor inteiro em segundos
# e imprima-o em horas, minutos e segundos.

# Libraries
import os

# Input
print("############## CONVERSOR DE TEMPO ##############")
print()
total = int(input("Digite um valor inteiro de quantos segundos você quiser: "))

# Processing
m = int(total / 60) # Ex.: total = 3600
    # m = 60
mr = int(m % 60)
    # mr = 0
h = int(m / 60) # 60 / 60
    # h 1
s = total - (h * 3600 + mr * 60)

# Output
print("Esse número é quivalente a %dh %dm e %ds" %(h, mr, s))
os.system("pause")