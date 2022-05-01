# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 21- Escreva o menu de opcoes abaixo. Leia a opcao do usuario e execute a operacao escolhida.
# Escreva uma mensagem de erro se a opcao for invalida. Escolha a opcao:
#     1- Soma de 2 numeros.
#     2- Difereca entre 2 numeros (maior pelo menor).
#     3- Produto entre 2 numeros.
#     4- Divisao entre 2 numeros (o denominador nao pode ser zero).

# Input
print("########## Calculadora ##########")
print()
print("Menu de opções")
print()
print("1- Soma de 2 números")
print("2- Difereça entre 2 nmeros (maior pelo menor)")
print("3- Produto entre 2 números")
print("4- Divisão entre 2 números (o denominador não pode ser 0)")
print()
opc = int(input("Opção: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
# Processing and Output
if(opc == 1):
    soma = n1 + n2
    print("A soma dos números é de: %.2f" %(soma))
elif(opc == 2):
    if(n1 > n2):
        sub = n1 - n2
        print("A subtração resulta em: %.2f" %(sub))
    elif(n2 > n1):
        sub = n2 - n1
        print("A subtração resulta em: %.2f" %(sub))
    else:
        print("O resultado é zero!")
elif(opc == 3):
    prod = n1 * n2
    print("O produto entre os números é de %.2f" %(prod))
elif(opc == 4):
    if(n2 != 0):
        div = n1 / n2
        print("O resultado da divisão é de: %.2f" %(div))
    else:
        print("O denominador não pode ser 0!")
else:
    print("Opção Inválida!")