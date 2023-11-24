from aocd import get_data
file= get_data(day=3, year=2022)
alph1='abcdefghijklmnopqrstuvwxyz'
alph2=alph1.upper()
result=0
for line in file.splitlines():
    first=line[:len(line)//2]
    second=line[len(line)//2:]
    common=''.join(set(first).intersection(second))

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