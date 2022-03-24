# input
tempo = int(input())
velo = int(input())

# processing
dist = tempo*velo
gasto = dist / 12

# output
print("%.3f" %(gasto))