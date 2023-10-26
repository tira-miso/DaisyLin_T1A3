import os
import csv

def open_pokemon_csv(operation):

    pokemon_masterlist = "pokemonOG.csv"
    pokemon_csv_path = os.path.join(
        os.path.dirname(__file__), pokemon_masterlist)

    try:
        csv_file = open(pokemon_csv_path, operation)
        return csv_file

    except FileNotFoundError:
        print("File not found:", pokemon_csv_path)
        return None
    
# f = open('path/to/csv_file', 'w')

# # create the csv writer
# writer = csv.writer(csv_file:)
# writer.writerows(data)

with open_pokemon_csv('r') as csv_file:
   data = list(csv.reader(csv_file, delimiter=","))


headers = data[0]
first_gen = data[:152]
tbl_data = first_gen[1:]
user_created = data[153:]
