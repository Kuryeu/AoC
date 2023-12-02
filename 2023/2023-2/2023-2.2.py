from aocd import get_data
file= get_data(day=2, year=2023)
ans=0
for line in file.splitlines():
    print(line)
    id = line.split(" ")[1].replace(":","")
    tirages = line.split(":")[1]
    print(id)
    sets = tirages.split(";")
    blue=0
    red=0
    green=0
    for set in sets: 
        # print(set) 
        boules = set.split(",")
        for boule in boules:

            nombre = int(boule.split(" ")[1])
            print(nombre)
            color = boule.split(" ")[-1]
            # print(nombre, color)
            if color == "blue":
                if nombre>blue:
                    blue = nombre
            if color == "red":
                if nombre>red:
                    red = nombre

            if color == "green":
                if nombre>green:
                    green = nombre

    ans+=red*blue*green
        
print(ans)