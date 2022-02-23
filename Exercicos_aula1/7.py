# FATEC - Segurança da Informação
# AULA 1 - Introdução a lógica
# Prof: Rogério Lazanha
# Augusto Finotti Oliveira 23/02/2022

# Bibliotecas
import os

# 7- Calcule a média final (média ponderada) da disciplina de lógica de programação
# sabendo que o aluno tem de nota final das provas o valor de 8 e de nota final
# dos trabalhos o valor 7. (fórmula:  )

# Entrada
np = float(input("Digite a nota da prova do aluno: "))
nt = float(input("Digite a nota do trabalho do aluno: "))

# Processamento
mf = (np * 0.7) + (nt * 0.3)

# Saída
print("A média final do aluno será de %.1f" %(mf))
os.system("pause")
