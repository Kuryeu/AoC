from aocd import get_data
file= get_data(day=4, year=2022)
count=0
for line in file.splitlines():
    a = line.split(',')[0]
    b = line.split(',')[1]
    ax = int(a.split('-')[0])
    ay = int(a.split('-')[1])
    bx = int(b.split('-')[0])
    by = int(b.split('-')[1])

    if (ax <= bx and ay >= by) or (bx <= ax and by >= ay):
        count+=1
        
print(count)