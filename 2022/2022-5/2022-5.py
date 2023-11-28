#Step 1 : Create initial lists
initial = open('initial', "r").readlines()

columns = zip(*[line for line in initial])
setup= {}
for column in columns:
    if column[len(column)-1].isdigit() == True:
        name=f'col_{column[len(column)-1]}'
        cleanColumn =[]
        for x in column:
            if x!=' ':
                cleanColumn+=x
        cleanColumn.pop()
        setup[name]=cleanColumn

print(setup)

#Step 2 : Iterate through instructions
def MoveElement(fromList, toList):
    toList.insert(0,fromList.pop(0))

instructions = open('instructions', "r").readlines()
for line in instructions:
    line = line.strip()
    number = line.split(' ')[1]
    fraume = line.split(' ')[3]
    to =line.split(' ')[5]

    colNameFrom=f'col_{fraume}'
    colNameTo=f'col_{to}'

    for i in range(int(number)):
        MoveElement(setup[colNameFrom],setup[colNameTo])

print(setup)

#Step 3 : create answer
ans = ''
for i in setup:
    ans+=setup[i][0]

print(ans)