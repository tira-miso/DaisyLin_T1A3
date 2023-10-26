import csv_module
from search import search_method
from randompokemon import random_pokemon
from tabulate import tabulate



def terminal_menu():
    user_input = input("""
Welcome to Pokédex, we help you find your Pokémon.
                       
Enter [1] to display all Pokémons.
Enter [2] to search Pokémons.
Enter [3] to get a random Pokémon.
Enter [4] to add a Pokémon.
Enter [5] to display search history.\n
""")

    if int(user_input) == 1:
        print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
    elif int(user_input) == 2:
        search_method(tbl_data, headers)
    elif int(user_input) == 3:
        random_pokemon(tbl_data, headers)

    select_option()

def select_option():
    user_input = input(
        '\nEnter [1] to go back to main menu.\nEnter [2] to finish the program.\n')

    if int(user_input) == 2:

        print('Thanks for using Pokédex. We hope to see you again.\n')
        global running
        running = False
        

if __name__ == "__main__":

    running = True
    
    while running:
        terminal_menu()
        
