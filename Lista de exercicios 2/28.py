# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 28 - Faca um programa que leia tres numeros inteiros positivos e efetue o calculo de uma das
# seguintes medias de acordo com um valor numerico digitado pelo usuario

# Input
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))
print("Qual média você deseja realizar?")
print("")
print("[ a ]    - Geométrica")
print("[ b ]    - Ponderada")
print("[ c ]    - Harmônica")
print("[ d ]    - Aritmética")
print("")
op = input("Opção desejada: ")
# Processing and Output
if(op == "a"):
    res = pow((x * y * z), 1/3)
    print("Logo, o resultado é: %.2f" %(res))
elif(op == "b"):
    res = (x + (2*y) + (3*z))/6
    print("Logo, o resultado é: %.2f" %(res))
elif(op == "c"):
    res = 1/((1/x)+(1/y)+(1/z))
    print("Logo, o resultado é: %.2f" %(res))
elif(op == "d"):
    res = (x+y+z)/3
    print("Logo, o resultado é: %.2f" %(res))
else:
    print("Opção inválida!")