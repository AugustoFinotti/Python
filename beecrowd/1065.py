v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
num_par = 0
if(v1%2) == 0:
    num_par = num_par +1
if(v2%2) == 0:
    num_par = num_par +1
if(v3%2) == 0:
    num_par = num_par +1
if(v4%2) == 0:
    num_par = num_par +1
if(v5%2) == 0:
    num_par = num_par +1
num_par = int(num_par)
print("%d valores pares" %(num_par))