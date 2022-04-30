# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 2- Leia um numero fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do numero.
# Se o numero for negativo, mostre uma mensagem dizendo que o numeroe invalido.

# Input
num = float(input("Digite um número: "))
# Processing and Output
if(num>0):
    res = pow(num, 0.5)
    print("A raiz quadrada desse número é: %.2f" %(res))
else:
    print("O número digitado é inválido!")