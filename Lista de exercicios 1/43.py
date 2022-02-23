# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 43. Escreva um programa de ajuda para vendedores. 
# A partir de um valor total lido, mostre:
#   • o total a pagar com desconto de 10%;
#   • o valor de cada parcela, no parcelamento de 3× sem juros;
#   • a comissao do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
#   • a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

# Bibliotecas
import os

# Input
print("############## Ajuda para Vendedores ##############")
print()
vl_t = float(input("Digite o valor total: "))

# Processing
vl_des = vl_t * 0.90    # valor com desconto de 10% na compra á vista
vl_par = vl_t / 3       # valor de cada parcela - 3 parcelas (sem desconto)
com_vis = vl_des * 0.05 # comissão da venda feita sob o valor á vista
com_par = vl_t * 0.05   # comissão da venda feita sob o valor sem deconto

# Output
print("O valor total a pagar com 10 por cento de desconto é de: %.2f R$" %(vl_des))
print("Dividindo em 3 vezes, o valor de cada parcela será de: %.2f R$" %(vl_par))
print("A comissão para Vendedores será de %.2f R$ nas compras com desconto" %(com_vis))
print("A comissão para Vendedores será de %.2f R$ nas compras parceladas" %(com_par))
os.system("pause")