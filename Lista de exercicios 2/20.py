# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 20- Dados tres valores: A, B, C, verificar se eles podem ser valores dos lados de um triangulo
# e, se forem, se e um triangulo escaleno, equilatero ou isoscele, considerando os seguintes conceitos:
#     • O comprimento de cada lado de um triangulo e menor do que a soma dos outros dois lados.
#     • Chama-se equilatero o triangulo que tem tres lados iguais.
#     • Denominam-se isosceles o triangulo que tem o comprimento de dois lados iguais.
#     • Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.

# Input
a = float(input("Digite o valor de um lado do triângulo: "))
b = float(input("Digite o valor do sengundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))
print()
# Processing and Output
if(a < b + c) and (b < a + c) and (c < b + a):
    if(a == b) and (b == c):
        print("Triângulo Equilátero!")
    elif(a == b) or (b ==c) or (a == c):
        print("Triângulo Isóceles!")
    else:
        print("Triângulo Escaleno!")
else:
    print("Não é possível formar um triângulo!")
print()