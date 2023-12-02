from aocd import get_data
file= get_data(day=1, year=2023)

ans=0
for line in file.splitlines():
    number=""
    for i in range(0, len(line)):
        # print(val)
        line.lower()
        if line[i].isdigit():
            number+=line[i]
        if len(line)-1-i >=4:
            if line[i] == 't' and line[i+1]=='h' and line[i+2]=='r' and line[i+3]=='e' and line[i+4]=='e':
                number+='3'
            if line[i] == 's'and line[i+1]=='e' and line[i+2]=='v' and line[i+3]=='e' and line[i+4]=='n':
                number+='7'
            if line[i] == 'e'and line[i+1]=='i' and line[i+2]=='g' and line[i+3]=='h' and line[i+4]=='t':
                number+='8'
        if len(line)-1-i >=3:
            if line[i] == 'f' and line[i+1]=='o' and line[i+2]=='u' and line[i+3]=='r':
                number+='4'
            if line[i] == 'f'and line[i+1]=='i' and line[i+2]=='v' and line[i+3]=='e':
                number+='5'
            if line[i] == 'n'and line[i+1]=='i' and line[i+2]=='n' and line[i+3]=='e':
                number+='9'
        
        if len(line)-1-i >=2:
            if line[i] == 'o'and line[i+1]=='n' and line[i+2]=='e': 
                number+='1'
            if line[i] == 't'and line[i+1]=='w' and line[i+2]=='o':
                number+='2'
            if line[i] == 's'and line[i+1]=='i' and line[i+2]=='x':
                number+='6'
    if len(number):
        value = number[0] + number[-1]
    ans+=int(value)
print(ans)