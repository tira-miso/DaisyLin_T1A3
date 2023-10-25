import csv

# Getting all data from CSV
data = []
with open('pokemonOG.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)


def search_name():
    name = input('Enter a Pokémon name: \n')
# Getting a list of everything in the name column 
    col = [x[1] for x in data]
    if name in col:
        for x in range(0,len(data)):
            if name == data[x][1]:
                print(data[x])

    else:
        print("Name doesn't exist.")
