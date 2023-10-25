from tabulate import tabulate 
# Getting all data from CSV
# data = []
# with open_pokemon_csv() as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         data.append(row)

def search_method(data, fullheaders):
    user_input = input(
       'Enter [1] to search by name.\nEnter [2] to search by number.\nEnter [3] to search by type.\n\n')
    if int(user_input) == 1:
        search_name(data, fullheaders)
    elif int(user_input) == 2:
        search_num(data, fullheaders)
    elif int(user_input) == 3:
        search_type(data, fullheaders)


def search_name(data, fullheaders):
    name = input('Enter a Pokémon name: \n')

    col = [x[1] for x in data]
    if name in col:
        index = col.index(name)        
        # for x in range(0,len(data)):
        #     if name == data[x][1]:
        print(tabulate([data[index]], headers= fullheaders, tablefmt="fancy_grid"))

    else:
        print("Name doesn't exist.")

def search_num(data, fullheaders):
    number = input('Enter a Pokémon ID: \n')

    col = [x[0] for x in data]
    if number in col:
        index = col.index(number)        
       
        print(tabulate([data[index]], headers= fullheaders, tablefmt="fancy_grid"))


def search_type(data, fullheaders):
    type = input('Enter a Pokémon type, \nBug, Dragon, Electric, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, or Water: \n')

    # col = [x[2] for x in data]
    # if type in col:
    #     index = col.index(type)      
    
       
        print(tabulate([data[index]], headers= fullheaders, tablefmt="fancy_grid"))

