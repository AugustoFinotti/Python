# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 03/05/2022

# 33- Um produto vai sofrer aumento de acordo com a tabela abaixo.
# Leia o preco antigo, calcule e escreva o preco novo, e escreva uma mensagem em funcao do preco novo
# (de acordo com a segunda tabela).
# PRECO ANTIGO           |      PERCENTUAL DE AUMENTO
# ate R$ 50              |              5%
# entre R$ 50 e R$ 100   |              10%
# acima de R$ 100        |              15%

# Input
prec_ant = float(input("Digite o valor do preço antigo: "))
# Processing and Output
if(prec_ant < 50):
    aument = 1.05 # como é um aumento será acrescentado 5% ao montante anterior, logo 0.05 + 1.00 = 1.05
elif(prec_ant >= 50) and (prec_ant<=100):
    aument = 1.1
else:
    aument = 1.15

prec_novo = prec_ant * aument
print("O preço novo será de: %.2f R$" %(prec_novo))