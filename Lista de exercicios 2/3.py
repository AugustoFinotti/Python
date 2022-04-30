# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 3- Leia um numero real. Se o numero for positivo imprima a raiz quadrada.
# Do contrario, imprima o numero ao quadrado.

# Input
num = int(input("Digite um número: "))
# Processing and Output
if(num>0):
    res = pow(num, 0.5)
    print("A raiz quadrada desse número é: %.2f" %(res))
else:
    res = num ** 2
    print("O número elevado ao quadrado resulta em: %.2f" %(res))