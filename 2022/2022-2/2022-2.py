with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

score=0
for line in lines:
    if line[-1] =='X':
        score+=1
        if line[0]=='A':
            score+=3
        if line[0]=='B':
            score+=0
        if line[0]=='C':
            score+=6
    if line[-1] =='Y':
        score+=2
        if line[0]=='A':
            score+=6
        if line[0]=='B':
            score+=3
        if line[0]=='C':
            score+=0
    if line[-1] =='Z':
        score+=3
        if line[0]=='A':
            score+=0
        if line[0]=='B':
            score+=6
        if line[0]=='C':
            score+=3
print(score)