n = int(input())
inside = 0
outside = 0
for x in range(n):
    val = int(input())
    if(val>=10) and (val<=20):
        inside += 1
    else:
        outside +=1
        
print("%d in" %(inside))
print("%d out" %(outside))
