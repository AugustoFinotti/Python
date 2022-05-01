# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 01/05/2022

# 22 -Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar.
# As condicoes para aposentadoria sao:
#     • Ter pelo menos 65 anos,
#     • Ou ter trabalhado pelo menos 30 anos,
#     • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

# Input
idade = int(input("Digite sua idade: "))
serv = int(input("Digite seu tempo de serviço em anos: "))
# Processing and Output
if(idade >= 65):
    print("Você já pode se aposentar!")
elif(serv >= 30):
    print("Você já pode se aposentar!")
elif(idade >= 60) and (serv >= 25):
    print("Você já pode se aposentar!")
else:
    print("Você não pode ser aposentar!")