from aocd import get_data
file= get_data(day=6, year=2022)
res=0
ok = True
for line in file.splitlines():
    count=1
    for i,char in enumerate(line):
        print(i, line[i],line[i-3],line[i-2],line[i-1])
        print('='*80)
        if i>4:
            previous = [line[i-3],line[i-2],line[i-1],char]
            cleanPrevious = set(previous)
            if len(previous) == len(cleanPrevious):
                res=count
                break
        count+=1
    print(res)