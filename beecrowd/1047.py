hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final )

if (hora_final == hora_inicial):
    if (minuto_final == minuto_inicial): # Exemplo de valores de entrada: 7 7 7 7
        hora = 24
        minuto = 0

    elif (minuto_final > minuto_inicial): # 7 2 7 4
        hora = 0
        minuto = minuto_final - minuto_inicial

    elif (minuto_inicial > minuto_final): # 7 4 7 2 
        hora = 23
        minuto = 60 - (minuto_inicial - minuto_final)

elif (hora_final > hora_inicial):
    hora = hora_final - hora_inicial

    if (minuto_final == minuto_inicial): # 6 5 7 5
        minuto = 0

    elif (minuto_final > minuto_inicial): # 6 5 7 6
        minuto = minuto_final - minuto_inicial

    elif (minuto_inicial > minuto_final): # 6 10 7 6
        minuto = 60 - (minuto_inicial - minuto_final)
        hora = hora - 1

if (hora_inicial > hora_final):
    hora = 24 - (hora_inicial - hora_final)
    if(minuto_final == minuto_inicial): # 7 5 6 5
        minuto = 0

    elif(minuto_final > minuto_inicial): # 7 0 6 2 
        minuto = minuto_final - minuto_inicial

    elif(minuto_inicial > minuto_final): # 7 2 6 1
        minuto = 60 - (minuto_inicial - minuto_final)
        hora = hora - 1

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hora, minuto))