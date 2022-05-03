# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 24 - Uma empresa vende o mesmo produto para quatro diferentes estados.
# Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
# Faca um programa em que o usuario entre com o valor e o estado destino do produto
# e o programa retorne o preco final do produto acrescido do imposto do estado em que ele sera vendido.
# Se o estado digitado nao for valido, mostrar uma mensagem de erro.

# Input
valor = int(input("Digite o valor do produto: "))
uf = input("Digite o estado de destino: ")
# Processing and Output
if(uf == "MG"):
    pre_fi = valor * 1.07
    print("O preço final do produto será de: %.2f" %(pre_fi))
elif(uf == "SP"):
    pre_fi = valor * 1.12
    print("O preço final do produto será de: %.2f" %(pre_fi))
if(uf == "RJ"):
    pre_fi = valor * 1.15
    print("O preço final do produto será de: %.2f" %(pre_fi))
if(uf == "MS"):
    pre_fi = valor * 1.08
    print("O preço final do produto será de: %.2f" %(pre_fi))
else:
    print("Esse estado é invalidado!")