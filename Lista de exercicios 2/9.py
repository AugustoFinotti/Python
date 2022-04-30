# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 30/04/2022

# 9- Leia o salario de um trabalhador e o valor da prestacao de um emprstimo.
# Se aprestacao for maior que 20% do salario imprima: Emprestimo nao concedido,
# caso contrario imprima: Emprestimo concedido.

# Input
sal = float(input("Digite o salário do trabalhador: "))
pres = float(input("Digite o valor da prestação do empréstimo: "))
# Processing and Output
if(pres * 0.2 >= sal):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")
