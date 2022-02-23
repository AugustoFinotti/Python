# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 23/02/2022

# 18- Calcule a média final (média ponderada) da disciplina de lógica de programação
# de acordo com a seguinte fórmula: média final = (nota da prova * 0.8 + nota do trabalho * 0.2) 

# Libraries
import os

# - - - - - - Input - - - - - - - 
print()
print("###########################################################")
print("### - - - - - - - - - - Média Final - - - - - - - - - - ###")
print("###########################################################")
print()
np = float(input("Digite a nota da prova do aluno: "))
nt = float(input("Digite a nota do trabalho do aluno: "))

# - - - - - Processing - - - - - 
mf = np * 0.8 + nt * 0.2

# - - - - - - Output - - - - - - 
print("A mpedia final desse aluno será de %.1f" %(mf))
os.system("pause")