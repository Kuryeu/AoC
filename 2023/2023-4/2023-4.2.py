from aocd import get_data
file= get_data(day=4, year=2023)
ans=0
for i, line in enumerate(file.splitlines()):
    loc=0.5
    win=False
    winning = str(line.split('|')[0]).split(':')[1][:-1]
    print(winning)
    print('='*80)
    card = str(line.split('|')[1])
    print(card)
    winning = winning.split(' ')
    for i in card.split(" "):
        if i in winning and i!="":
            win=True
            loc*=2
    if win==True:
        ans+=loc
        
print(ans)