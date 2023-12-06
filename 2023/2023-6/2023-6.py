ans=1
time = [50,74,86,85]
distance = [242,1017,1691,1252]

for i in range(len(time)):
    localAns=0
    speed=0
    for x in range(1,time[i]):
        speed+=1
        d= speed*(time[i]-x)
        if d>distance[i]:
            localAns+=1
    
    ans*=localAns
print(ans)