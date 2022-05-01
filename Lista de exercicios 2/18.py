# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 18- Faca um programa que mostre ao usuario um menu com 4 opcoes de operacoes matematicas
# (as basicas, por exemplo). O usuario escolhe uma das opcoes e o seu programa entao
# pede dois valores numericos e realiza a operacao, mostrando o resultado e saindo.

# Input
print("########## Software matemático ##########")
print()
print("Qual operação você deseja realizar?")
print("     [ 1 ] soma")
print("     [ 2 ] subtração")
print("     [ 3 ] multiplicação")
print("     [ 4 ] divisão")
print()
ope = int(input(" "))
print()
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o Segundo valor: "))
# Processing and Output
if(ope == 4):
    res = n1 / n2
    print("O resultado da divisão entre os valores é: %.2f" %(res))
elif(ope == 3):
    res = n1 * n2
    print("O resultado da multiplicação entre os valores é: %.2f" %(res))
elif(ope == 2):
    res = n1 - n2
    print("O resultado da subtração entre os valores é: %.2f" %(res))
elif(ope == 1):
    res = n1 + n2
    print("O resultado da adição entre os valores é: %.2f" %(res))
else:
    print("Opção inválida!")