# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 25 -  Calcule as raızes da equacao de segundo grau. Lembrando que:
# x = −b ±√ ∆
#     2a
# Onde   ∆ = B^2 − 4ac
# E ax2 + bx + c = 0 representa uma equacao de segundo grau.
# A variavel a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Nao eh equacao de segundo grau”.
#   • Se ∆ < 0, nao existe real. Imprima a mensagem Nao existe raiz.
#   • Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz unica.
#   • Se ∆ > 0, imprima as duas raızes reais.

# Input
print("Vamos calcular as possíveis raízes de uma equação do segundo grau")
a = float(input("Digite o valor de A na equação: "))
# - A tem que ser != de 0
if(a == 0):
    print("Não é equação do segundo grau!")
# continuando o programa apenas se A for != de 0
else:
    b = float(input("Digite o valor de B na equação: "))
    c = float(input("Digite o valor de C na equação: "))
    delta = b**2 - (4 * a * c)
    if(delta < 0):
        print("Não existe raíz!")
    elif(delta == 0):
        x = (-b - pow(delta, 0.5)) / 2*a
        print(x)
        print("Raíz única")
    else: # delta > 0
        x1 = (-b + pow(delta, 0.5)) / 2*a
        x2 = (-b - pow(delta, 0.5)) / 2*a
        print("As raízes são")
        print(x1)
        print(x2)

