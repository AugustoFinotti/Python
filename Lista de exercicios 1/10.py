# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 10- Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s
# (metros por segundo). A formula de conversão é: M = K/3.6, sendo K a velocidade em
# km/h e M em m/s.

# Input
print("############## Conversor de km/h para m/s ##############")
print()
K = float(input("Digite a velocidade em Km/h: "))

# Processing
M = K/3.6 

# Output
print("A velocidade equivalente em m/s é: %.2f m/s" %(M))
