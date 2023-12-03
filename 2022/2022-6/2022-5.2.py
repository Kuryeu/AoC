from aocd import get_data
file= get_data(day=6, year=2022)
res=0
count=1
for i,char in enumerate(file):
    print('='*80)
    print(i)
    previous = []
    if i>13:
        previous=file[count-14:count]
        cleanPrevious = set(previous)
        print(sorted(previous), sorted(cleanPrevious))
        if sorted(previous) == sorted(cleanPrevious):
            res=count
            index = file.index(char)
            break
    count+=1
print(res)