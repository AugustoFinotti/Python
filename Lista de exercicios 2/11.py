# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 11- Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
# soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponder ao valor
# 8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa terminar a com a
# mensagem “Numero invalido”. 

# Input
num = int(input("Digite um número: "))
# Processing and Output
soma = 0
if(num > 0):
    while(num>0):
        soma = soma + num % 10
        num = num // 10
    print("A soma dos algarismos é: %d" %(soma))
else:
    print("Número Inválido")