# Entrada
v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())
# Processamento
num_par = 0
v_total = 0
if(v1!=0) and (v1%2) == 0:
    num_par = num_par +1
    v_total = v_total + v1
if(v2!=0) and (v2%2) == 0:
    num_par = num_par +1
    v_total = v_total + v2
if(v3!=0) and (v3%2) == 0:
    num_par = num_par +1
    v_total = v_total + v3
if(v4!=0) and (v4%2) == 0:
    num_par = num_par +1
    v_total = v_total + v4
if(v5!=0) and (v5%2) == 0:
    num_par = num_par +1
    v_total = v_total + v5
if(v6!=0) and (v6%2) == 0:
    num_par = num_par +1
    v_total = v_total + v6
num_par = float(num_par)
if(num_par!=0):
    media = v_total / num_par
    # Saída
    print("%d valores pares" %(num_par))
    print(media)