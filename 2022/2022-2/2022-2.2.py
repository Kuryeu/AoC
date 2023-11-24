with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

score=0
for line in lines:
    if line[0] =='A':
        if line[-1]=='X':
            score+=3
        if line[-1]=='Y':
            score+=4
        if line[-1]=='Z':
            score+=8
    if line[0] =='B':
        if line[-1]=='X':
            score+=1
        if line[-1]=='Y':
            score+=5
        if line[-1]=='Z':
            score+=9
    if line[0] =='C':
        if line[-1]=='X':
            score+=2
        if line[-1]=='Y':
            score+=6
        if line[-1]=='Z':
            score+=7
print(score)