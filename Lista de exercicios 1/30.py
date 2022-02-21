# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 16/02/2022

# 30- Leia um valor em real e a cotação do dólar.
# Em seguida, imprima o valor correspondente em dólares. 

# Input
print("$$$$$$$$$$$$$$ Conversor de Reais em Dólares $$$$$$$$$$$$$$")
print()
r = float(input("Digite a quantia em Reais a ser convertida: "))
cot = float(input("Digite a cotação do dólar hoje: "))

# Processing
dol = r / cot

# Output
print("Essa quantia em Reais é equivalente a %.2f dólares hoje" %(dol))
