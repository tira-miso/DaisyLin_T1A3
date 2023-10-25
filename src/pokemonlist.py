import csv
from csv_module import open_pokemon_csv

def pokemon_listr(): 

    with open_pokemon_csv() as csv_file:
        pokemon_csv_file = csv.DictReader(csv_file)

        for line in pokemon_csv_file:
            print(line['Number'], line['Name'])

