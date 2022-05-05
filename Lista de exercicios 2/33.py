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
print()

#      PRECO NOVO       |    MENSAGEM
#      ate R$ 80              Barato
#
# entre R$ 80 e R$ 120
#     (inclusive)             Normal

# entre R$ 120 e R$ 200
#     (inclusive)             Caro
#
# acima de R$ 200             Muito caro

if(prec_novo<80):
    print("Barato")
elif(prec_novo>=80) and (prec_novo<=120):
    print("Normal")
elif(prec_novo>120) and (prec_novo<=200):
    print("Caro")
else:
    print("Muito caro")