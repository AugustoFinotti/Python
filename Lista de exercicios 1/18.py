# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 18- Leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros.
# A formula de conversão é: L = 1000 * M, sendo L o volume em litros
# e M o volume em metros cubicos. 

# Input
print("############## Conversor de metros cúbicos para litros ##############")
print()
M = float(input("Digite o valor do volume em metros cúbicos: "))

# Processing
L = M * 1000

# Output
print("O valor equivalente em litros é de %.2f L" %(L))
