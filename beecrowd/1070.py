x = int(input())
if(x%2==0):
    comeco = x + 1
else:
    comeco = x
fim = comeco + 11
for n in range(6):
    print("%d" %(comeco))
    comeco += 2