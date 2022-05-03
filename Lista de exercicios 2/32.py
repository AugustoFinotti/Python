# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 32 - Escrever um programa que leia o codigo do produto escolhido do cardapio de uma lanchonete e a quantidade.
# O programa deve calcular o valor a ser pago por aquele lanche.
# Considere que a cada execucao somente sera calculado um pedido.
# O cardapio da lanchonete segue o padrao abaixo:
# Especificacao   |  Codigo | Preco
# Cachorro Quente     100     1.20
# Bauru Simples       101     1.30
# Bauru com Ovo       102     1.50
# Hamburguer          103     1.20
# Cheeseburguer       104     1.70
# Suco                105     2.20
# Refrigerante        106     1.00


# Input
print("############## Cardápio ##############")
print()
print("     Nome          Código    Preço")
print("Cachorro Quente     100     1,20 R$")
print("Bauru Simples       101     1,30 R$")
print("Bauru com Ovo       102     1,50 R$")
print("Hambúrguer          103     1,20 R$")
print("Cheeseburguer       104     1,70 R$")
print("Suco                105     2,20 R$")
print("Refrigerante        106     1,00 R$")
print()
cod = int(input("Digite o código do produto desejado: "))
quant = int(input("Digite a quantidade do produto desejado:  "))
# Processing and Output
if(cod==100):
    prec = 1.2
elif(cod==101):
    prec = 1.3
elif(cod==102):
    prec = 1.5
elif(cod==103):
    prec = 1.2
elif(cod==104):
    prec = 1.7
elif(cod==105):
    prec = 1.2
elif(cod==106):
    prec = 1.0 
else:
    print("Código inválido!")
total = quant*prec
print("Seu pedido ficou em total de: %.2f R$"%(total))