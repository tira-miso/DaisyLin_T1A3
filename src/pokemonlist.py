from tabulate import tabulate 

def pokemon_listr(data): 

    id_name_list = [row[0:3] for row in data]
    print(tabulate(id_name_list, headers="firstrow", tablefmt="fancy_grid"))

