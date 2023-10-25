from pokemonlist import pokemon_listr


def terminal_menu():
    print('\nWelcome to Pokédex, we help you find your Pokémon.\n')
    user_input = input(
        'Enter [1] to display all Pokémons.\nEnter [2] to search Pokémons.\nEnter [3] to get a random Pokémon.\nEnter [4] to add a Pokémon.\nEnter [5] to display search history.\n\n')

    if int(user_input) == 1:
        pokemon_listr()


def select_option():
    user_input = input(
        '\nEnter [1] to go back to main menu.\nEnter [2] to finish the program.\n')

    if int(user_input) == 1:
        terminal_menu()
    else:
        print('Thanks for using Pokédex. We hope to see you again.\n')


terminal_menu()
select_option()
