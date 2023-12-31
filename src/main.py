import config as cg
import csv_module as cm
from search import main_search_loop
from randompokemon import random_pokemon
from tabulate import tabulate


def close_pokedex():
    print('Thanks for using Pokédex. We hope to see you again.\n')
    cg.main_run = False


def terminal_menu():
    print('Welcome to Pokédex, we help you find your Pokémon.')
    user_input = input(cg.menu)
    c = 0

    while user_input not in ['1', '2', '3', '4', '5']:
        if c % 5 == 0 and c != 0:
            user_input = input(cg.error_message + cg.menu)
        else:
            user_input = input(cg.error_message + '\n')
        c += 1

    user_input = int(user_input)

    if user_input == 1:
        print('Original 151 Pokémon:')
        print(tabulate(cm.data, headers='firstrow', tablefmt='fancy_grid'))
        if len(cm.user_created) > 1:
            print('User Added Pokémon:')
            print(tabulate(cm.user_created, headers='firstrow', tablefmt='fancy_grid'))
        select_option()
    elif user_input == 2:
        main_search_loop()
    elif user_input == 3:
        random_pokemon()
        select_option()
    elif user_input == 4:
        print(cg.func_unavaible)
        select_option()
    elif user_input == 5:
        close_pokedex()


def select_option():
    selection = input(
        '\nEnter [1] to go back to main menu.\nEnter [2] to finish the program.\n')
    while selection not in ['1', '2']:
        selection = input(cg.error_message + '\n')
    selection = int(selection)
    if selection == 1:
        terminal_menu()
    elif selection == 2:
        close_pokedex()


if __name__ == "__main__":

    cg.main_run = True

    while cg.main_run:
        terminal_menu()
