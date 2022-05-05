# FATEC Ourinhos - Programação 1 - Seg Info
# Augusto Finotti Oliveira
# Prof. Rogério Lazanha
# 05/05/2022

# 35 - Leia uma data e determine se ela e valida. Ou seja, verifique se o mes esta entre 1 e 12,
# e se o dia existe naquele mes. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos nao bissextos.
# Sendo que um ano e bissexto se for divisıvel por 400 ou se for divisıvel por 4 e nao for divisıvel por 100.

# Calendário usado de base
#     MÊS       |  DIAS
# 1- Janeiro       31
# 2- Fevereiro     28      (bissexto: 29)
# 3- Março         31
# 4- Abril         30
# 5- Maio          31
# 6- Junho         30
# 7- Julho         31
# 8- Agosto        31
# 9- Setembro      30
# 10- Outubro      31
# 11- Novembro     30
# 12- Dezembro     31

#  - - - Input - - - #
# recebendo 3 variáveis em uma linha só com o .split()
dia, mes, ano = (input("Digite uma data (dd mm aa): ")).split()

# - - - Processing - - - #
# transformando as variáveis em inteiras em uma linha só, respectivamente
dia, mes, ano = int(dia), int(mes), int(ano)

# controladores para a exibição (1 = verdadeiro, 0 = falso)
result, ano_bi = 0, 0 # result (data válida = 1, data inválida = 0) | ano_bi (ano bissexto = 1, ano normal = 0))

# averiguando o mês
if(mes>=1) and (mes<=12):

    # averiguando se é ano bissexto
    if(ano%400==0) or (ano%4==0 and (not ano%100==0)):
        ano_bi = 1 # ano é bissxexto

        # agora averiguando meses do calendario bissexto
        # Meses de 31 dias - Jan, Mar, Mai, Jul, Ago, Out e Dez
        if(mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if(dia>=1) and (dia<=31):
                result = 1 # data válida , portanto o resultado vai ser = 1, ou seja, verdadeiro
            else:
                result = 0 # data inválida, dia fora do intervalo de 1 e 31

        if(mes == 2): # FEVEREIRO - 29 dias
            if(dia>=1) and (dia <= 29): # averiguando os dias de FEVEREIRO bissexto
                result = 1 # data válida
            else:
                result = 0 # Data Inválida! - dias de janeiro fora do intervalo (1-29)

        # Meses de 30 dias
        if(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if(dia>=1) and (dia<=30):
                result = 1
            else:
                result = 0

    else: # ano não é bissxexto
        ano_bi = 0 

        # Meses de 31 dias - Jan, Mar, Mai, Jul, Ago, Out e Dez
        if(mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) (mes == 12):
            if(dia>=1) and (dia<=31):
                result = 1 # data válida , portanto o resultado vai ser = 1, ou seja, verdadeiro
            else:
                result = 0 # data inválida, dia fora do intervalo de 1 e 31

        if(mes == 2): # FEVEREIRO - 28 dias
            if(dia>=1) and (dia <= 29): # averiguando os dias de feveiro não bissexto
                result = 1 # data válida
            else:
                result = 0 # Data Inválida! - dias de fevereiro fora do intervalo (1-28)

        # Meses de 30 dias
        if(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if(dia>=1) and (dia<=30):
                result = 1
            else:
                result = 0

else:
    result = 0 # Data Inválida! - mês menor ou igual a 0 ou maior que 12 não existe

#  - - - Output - - - #
# armazenando possíveis saídas em variáveis em uma linha só, espectivamente, depois será preciso só exibir essa variáveis 
invalida, valida, bissexto, n_bissexto = "Data inválida!", "Data válida.", "Esse é um ano bissexto.", "Esse não é um ano bissexto."

if(result == 1): # se o ano for válido 
    # será exibido a mensagem de valides e se o ano é bissexo ou não
    if(ano_bi == 1):
        print(valida, bissexto)
    else:
        print(valida, n_bissexto)
else:
    # se o resultado não foi válido apenas será exibida a mensagem de invalidez da data
    print(invalida)