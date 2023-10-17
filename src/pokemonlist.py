import csv

def pokemon_listr(): 
  with open('pokemonOG.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['Number'], line['Name'])

# def select_option():
#    user_input = input('Enter [1] to go back to main menu.\nEnter [2] to finish the program.\n')


