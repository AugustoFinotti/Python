# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 28- Faça a leitura de tres valores e apresente como resultado a soma
# dos quadrados dos tres valores lidos. 

# Input
print("############## Soma de 3 quadrados ##############")
print()
v1 = float(input("Digite um valor: "))
v2 = float(input("Digite um segundo valor: "))
v3 = float(input("Digite um terceiro valor: "))

# Processing

# - - 3 soluções possíveis - -

# soma = v1**2 + v2**2 + v3**2
# soma = pow(v1, 2) + pow(v2, 2) + pow(v3, 2)
soma =  v1*v1 + v2*v2 + v3*v3

# Output
print("A soma dos quadrados dos três valores apresentados é de %.2f" %(soma))
