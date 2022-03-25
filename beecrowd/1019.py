N = int(input())

H = N // 3600
N = N % 3600
M = N // 60 
N = N % 60
S = N 

print("%d:%d:%d" %(H,M,S))