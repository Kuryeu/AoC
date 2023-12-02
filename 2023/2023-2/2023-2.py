from aocd import get_data
file= get_data(day=2, year=2023)
ans=0
for line in file.splitlines():
    print(line)
    id = line.split(" ")[1].replace(":","")
    tirages = line.split(":")[1]
    print(id)
    sets = tirages.split(";")
    for set in sets: 
        # print(set) 
        boules = set.split(",")
        for boule in boules:

            nombre = int(boule.split(" ")[1])
            print(nombre)
            color = boule.split(" ")[-1]
            # print(nombre, color)
            if color == "blue":
                if nombre>14:
                    id = 0
            if color == "red":
                if nombre>12:
                    id = 0

            if color == "green":
                if nombre>13:
                    id = 0

    ans+=int(id)
        
print(ans)