# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 21/02/2022

# 53- Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
# bem como o preço do metro de tela p.
# Imprima o custo para cercar este mesmo terreno com tela.

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - Preço da cerca de tela - - - - - - - ###")
print("###########################################################")
print()
c = float(input("Digite o valor do comprimento do terreno em metros: "))
l = float(input("Digite o valor da largura do terreno em metros: "))
vt = float(input("Digite o valor do preço por metro de tela R$: "))
print()

# - - - - - Processing - - - - - 
# perimetro = c*2 + l*2
# custo = perimetro * vt

custo = (c*2 + l*2) * vt

# custo = (c + c + l + l) * vt

# - - - - - - Output - - - - - - 
print("Considerando essas medidas e esse preço, o cercado de tela custará R$ %.2f" %(custo))
os.system("pause")