# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 17- Leia um valor de comprimento em centımetros e apresente-o convertido em polegadas.
# A formula de conversão é: P = C / 2.54 , sendo C o comprimento em centımetros
# e P o comprimento em polegadas.

# Input
print("############## Conversor de centímetros para polegadas  ##############")
print()
C = float(input("Digite o valor da distância em centímetros: "))

# Processing
P = C / 2.54

# Output
print("O valor equivalente é de %.2f polegada(s)" %(P))
