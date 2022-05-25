pos_val = 0
soma = 0

for n in range(6):
    num = float(input())
    if(num>0):
        pos_val += 1
        soma += num

media = soma / pos_val
print("%d valores positivos" %(pos_val))
print("%.1f" %(media))