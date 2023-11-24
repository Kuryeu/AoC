from aocd import get_data
file= get_data(day=3, year=2022)
alph1='abcdefghijklmnopqrstuvwxyz'
alph2=alph1.upper()
result=0
c=3
lines=file.splitlines()
for i in range(len(lines)):
    c+=1
    if (c-1)%3==0:
        f=lines[i]
        s=lines[i+1]
        t=lines[i+2]
        common=''.join(set(f).intersection(s).intersection(t))
        print(common)

        count=0
        for x in alph1:
            count+=1
            if (common==x):
                result+=count
        for y in alph2:
            count+=1
            if (common==y):
                result+=count


print(result)