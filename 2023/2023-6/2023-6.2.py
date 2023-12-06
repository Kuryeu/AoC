from aocd import get_data
file= get_data(day=6, year=2023)
ans=0
for x, line in enumerate(file.splitlines()):
    print(line)
print(ans)