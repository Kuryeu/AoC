from aocd import get_data
file= get_data(day=1, year=2023)

ans=0
for line in file.splitlines():
    number=""
    for val in line:
        # print(val)
        if val.isdigit():
            number+=val
    number = number[0] + number[-1]
    ans+=int(number)
submit(ans)