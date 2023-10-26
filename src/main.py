import config as cg
import csv_module as cm
from search import main_search_loop
from randompokemon import random_pokemon
from tabulate import tabulate

def close_pokedex():
    print('Thanks for using Pokédex. We hope to see you again.\n') 
    cg.main_run = False

def terminal_menu():
    user_input = input("""
Welcome to Pokédex, we help you find your Pokémon.
                       
Enter [1] to display all Pokémon.
Enter [2] to search Pokémon.
Enter [3] to get a random Pokémon.  
Enter [4] to add your own Pokémon.
                       
Enter [5] to Close Pokédex.                      

""")

    if int(user_input) == 1:
        print(tabulate(cm.data, headers="firstrow", tablefmt="fancy_grid"))
        select_option()
    elif int(user_input) == 2:
        main_search_loop()
    elif int(user_input) == 3:
        random_pokemon()
        select_option()
    elif int(user_input) == 5:
        close_pokedex()
    else: 
        print(cg.error_message)

    
def select_option():
    selection = input('\nEnter [1] to go back to main menu.\nEnter [2] to finish the program.\n')
    if selection not in [1, 2]:
        print(cg.error_message)
    elif int(selection) == 1:
        terminal_menu()
    elif int(selection) == 2:
        close_pokedex()
        

if __name__ == "__main__":

    cg.main_run = True
    
    while cg.main_run:
        terminal_menu()
        
