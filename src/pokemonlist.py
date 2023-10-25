import csv

def pokemon_listr(): 
    with open('pokemonOG.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['Number'], line['Name'])

