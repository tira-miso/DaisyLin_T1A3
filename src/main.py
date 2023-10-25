import os, csv
from pokemonlist import pokemon_listr
from search import search_method
from randompokemon import random_pokemon

def open_pokemon_csv():

    pokemon_masterlist = "pokemonOG.csv"
    pokemon_csv_path = os.path.join(os.path.dirname(__file__), pokemon_masterlist)

    try: 
        csv_file = open(pokemon_csv_path, 'r')
        return csv_file
        
    except FileNotFoundError:
        print("File not found:", pokemon_csv_path)
        return None

with open_pokemon_csv() as csv_file:   
    data = list(csv.reader(csv_file, delimiter=","))
    tbl_data = data[1:]
    headers = data[0]


def terminal_menu():
    print('\nWelcome to Pokédex, we help you find your Pokémon.\n')
    user_input = input(
       'Enter [1] to display all Pokémons.\nEnter [2] to search Pokémons.\nEnter [3] to get a random Pokémon.\nEnter [4] to add a Pokémon.\nEnter [5] to display search history.\n\n')

    if int(user_input) == 1:
        pokemon_listr(data)
    elif int(user_input) == 2:
        search_method(tbl_data, headers)
    elif int(user_input) == 3:
        random_pokemon(data)


def select_option():
    user_input = input(
        '\nEnter [1] to go back to main menu.\nEnter [2] to finish the program.\n')

    if int(user_input) == 1:
        terminal_menu()
 
    else:
        print('Thanks for using Pokédex. We hope to see you again.\n')


terminal_menu()
select_option()
