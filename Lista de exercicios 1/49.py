# FATEC Ourinhos - Segurança da Informação
# Programação 1 - Rogério Lazanha
# Augusto Finotti Oliveira
# 17/02/2022

# 49- Faça um programa para que leia o horário (hora, minuto e segundo)
# de inicio e a duração, em segundos, de uma experiencia biológica.
# O programa deve resultar com o novo horário (hora, minuto e segundo)
# do término da mesma.


# Input
print("############## Experiência Biológica ##############")
print()
print("Digite o horário que a experiência começou...")
h_in = int(input("Hora: "))
m_in = int(input("Minuto: "))
s_in = int(input("Segundo: "))

du = int(input("Digite quantos segundos a experiência vai durar: "))
print()

# Processing

#  - - - - transformando o segundos de duração - - - - - #
# minutos (para ser calculado nas horas)
m_calc = int(du // 60)
# segundos
s_du = int(du % 60)
# horas
h_du = int(m_calc // 60)
# minutos (restantes)
m_du = int(m_calc % 60)

# duração = (h_du) horas - (m_du) minutos - (s_du) segundos #

#  - - - - - estabelecendo o horario final - - - - - - - #
# horario final = horario inicial + duração)

# segundos para o calculo dos minutos
s_fin_calc = (s_in + s_du) // 60

# segundo final
s_fin = (s_in + s_du) % 60

# muinuto para o calculo das horas
m_fin_calc = (m_in + m_du + s_fin_calc) // 60

# minuto final
m_fin = (m_in + m_du + s_fin_calc) % 60

# hora para possível calculo dos dias
h_fin_calc = (h_in + h_du + m_fin_calc) 

# Se quiser transformar 24 horas em um dia:
# dias
dia = h_fin_calc // 24
# hora final
h_fin = h_fin_calc % 24

# Output

print("A duração da experiência será de: %d h %d m %d s" %(h_du, m_du, s_du))

# Se quiser mostrar também os dias corridos
# print("A experiência acabará %d dia(s) %d h %d m %d s" %(dia, h_fin, m_fin, s_fin))

print("A experiência acabará %d h %d m %d s" %(h_fin_calc, m_fin, s_fin))