import csv_module as cm
import config as cg
from tabulate import tabulate
from ast import literal_eval

history = cg.search_history

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

def main_search_loop():
    
    running = True
    
    while running:
        
        history_switch = input("[1] Search Pokemon \n[2] View Search History \n[3] Return to Main Menu \n")

        if int(history_switch) not in [1, 2, 3]:
            cg.Error_message
            
        elif int(history_switch) == 1:
            inner_search_loop()

        elif int(history_switch) == 2:
            if len(history) < 1:
                print('No search history! Please search some pokemon first.')
            else:
                print(tabulate(history,headers= ["Searches:","Results - ID:", "Result - Name:"], tablefmt="fancy_grid"))

        elif int(history_switch) == 3:
            running = False

def inner_search_loop():
    while True:
        user_input = input('Enter a Pokémon name or ID number to search: ')
        input_type = get_type(user_input)

        result = search_pokemon(user_input, input_type)
        history.append([user_input] + result)

        user_question = input('Do you want to search again? [Y]/[N]: ')
        while user_question.upper() not in ["Y", "N"]:
            user_question = input('Please enter "Y" or "N".\n')

        if user_question.upper() == "N":
            break

def search_pokemon(id, type):

    if type == str:
        col = 1
        id = id.lower()
    else:
        col = 0

    column = [x[col].lower() for x in cm.data]

    if id in column:
        i = column.index(id)
        print(tabulate([cm.data[i]], headers=cm.headers, tablefmt='fancy_grid'))
        return cm.data[i][:2]
    else:
        print("Pokémon doesn't exist.")
        return [None, None]
    
