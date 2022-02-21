# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 42- Receba o salário-base de um funcionário. Calcule e imprima o salário a receber
# sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
# Além disso ele paga 7% de imposto sobre o salario-base. 


# Input
print("############## Calculadora de Salário ##############")
print()
sal_ba = float(input("Digite o salário-base: "))

# Processing
sal_im = sal_ba * 0.07   # 7% (será subtaido posteriormente)
sal_gra = sal_ba * 0.05  # 5% (será adicionado posteriormente)
sal_fin = sal_ba - sal_im + sal_gra

# Output
print("Considerando um imposto de 7 por cento e uma gratificação de 5 por cento")
print("O salário a ser recebido é de R$ %.2f" %(sal_fin))