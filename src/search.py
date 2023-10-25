from tabulate import tabulate 
from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except(ValueError, SyntaxError):
        return str


    
def search_method(data, fullheaders):
    running = True
    
    while running:
        user_input = input('Enter a pokemon name or ID number to search\n\n')

        input_type = get_type(user_input)
        search_pokemon(user_input, input_type, data, fullheaders)
        
        while True:
            user_question = input('Do you want to search again? [Y]/[N] \n')

            if user_question.upper() == "Y":
                break
            elif user_question.upper() == "N":
                running = False
                break
            else:
                print('Please enter "Y" or "N".\n')



def search_pokemon(id, type ,data, fullheaders):

    if type == str:
        col = 1
        id = id.lower()
    else:
        col = 0
    
    column = [x[col].lower() for x in data]

    if id in column:
        i = column.index(id)        
     
        print(tabulate([data[i]], headers= fullheaders, tablefmt="fancy_grid"))

    else:
        print("Pokemon doesn't exist.")


    
    
    