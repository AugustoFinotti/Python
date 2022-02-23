# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 39- A importancia de R$ 780.000,0 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total:
#   • O primeiro ganhador receberá 46%;
#   • O segundo receberá 32%;
#   • O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

# Bibliotecas
import os

# Input
print("############## Premiação do Concurso ##############")
print()
print("A quantia de 780.000,0 R$ será dividida entre os 3 ganhadores...")
g1 = input("Digite o nome do primeiro ganhador: ")
g2 = input("Digite o nome do segundo ganhador: ")
g3 = input("Digite o nome do terceiro ganhador: ")

# Processing
p = 780000
p1 = p * 0.46
p2 = p * 0.32
p3 = p * (1.0 - (0.46 + 0.32)) 

# Output
print("A quantia destinada a %s é de R$ %.2f" %(g1, p1))
print("A quantia destinada a %s é de R$ %.2f" %(g2, p2))
print("A quantia destinada a %s é de R$ %.2f" %(g3, p3))
os.system("pause")