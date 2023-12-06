from aocd import get_data
file= get_data(day=6, year=2023)
ans=1
for x, line in enumerate(file.splitlines()):
    print(line)
print(ans)

time = [50748685]
distance = [242101716911252]

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