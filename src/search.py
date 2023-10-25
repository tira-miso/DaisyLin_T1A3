import csv
from csv_module import open_pokemon_csv

# Getting all data from CSV
data = []
with open_pokemon_csv() as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

def search_method():
    user_input = input(
       'Enter [1] to search by name.\nEnter [2] to search by number.\nEnter [3] to search by type.\n\n')
    if int(user_input) == 1:
        search_name()


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

