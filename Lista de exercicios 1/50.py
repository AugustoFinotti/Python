# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 19/02/2022

# 50- Implemente um programa que calcule o ano de nascimento de uma pessoa
# a partir de sua idade e do ano atual.


# Input
print("############## Ano de Nascimento ##############")
print()
ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite a sua idade: "))

# Processing
ano_nasc = ano_atual - idade

# Output
print("Considerando que você fez aniversário esse ano, o seu ano de nascimento é %d" %(ano_nasc))