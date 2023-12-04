from aocd import get_data
file= get_data(day=4, year=2023)

multi=[1]*219

def getScoreByCard(line: str):
    loc=0
    winning = str(line.split('|')[0]).split(':')[1][:-1]
    card = str(line.split('|')[1])
    winning = winning.split(' ')
    for i in card.split(" "):
        if i in winning and i!="":
            loc+=1
    return loc

def incrementMultiplier(multi: list, k: int, score:int):
    for i in range(1,score+1):
        multi[k+i]+=1*multi[k]
    return multi


for k, line in enumerate(file.splitlines()):
    score = getScoreByCard(line)
    multi = incrementMultiplier(multi, k, score)

print(sum(multi))