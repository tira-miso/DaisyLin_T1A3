import random
from tabulate import tabulate


def random_pokemon(data, fullheaders):
    chosen_row = random.choice(data)
    print(tabulate([chosen_row], headers=fullheaders, tablefmt="fancy_grid"))
