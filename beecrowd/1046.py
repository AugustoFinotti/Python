hi, hf = input().split()
hi = int(hi)
hf = int(hf)

if(hf>hi):
    dur = hf - hi
elif(hi==hf):
    dur = 24
elif(hi>hf):
    dur = 24 - hi + hf
    
print("O JOGO DUROU %d HORA(S)" %(dur))