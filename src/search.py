import csv_module as cm
from tabulate import tabulate
from ast import literal_eval


def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

def search_method():
    
    search_again_text = 'Do you want to search again? [Y]/[N]: '
    running = True

    while running:

        user_input = input('Enter a Pokémon name or ID number to search: ')
        input_type = get_type(user_input)

        if search_pokemon(user_input, input_type):
            user_question = input(search_again_text)
            while user_question.upper() not in ["Y", "N"]:
                user_question = input('Please enter "Y" or "N".\n')
            if user_question.upper() == "N":
                running = False
        else:
            print("Pokemon doesn't exist.")


def search_pokemon(id, type):

    if type == str:
        col = 1
        id = id.lower()
    else:
        col = 0

    column = [x[col].lower() for x in cm.data]

    if id in column:
        i = column.index(id)

        print(tabulate([cm.data[i]], headers=cm.headers, tablefmt="fancy_grid"))
        return True
    
