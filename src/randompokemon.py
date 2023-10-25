import random
from tabulate import tabulate 

def random_pokemon(data):
    chosen_row = random.choice(data)
    print(tabulate(chosen_row), headers="firstrow", tablefmt="fancy_grid")


