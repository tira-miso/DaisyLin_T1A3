import random
import csv_module as cm
from tabulate import tabulate


def random_pokemon():
    chosen_row = random.choice(cm.data)
    print(tabulate([chosen_row], headers=cm.headers, tablefmt="fancy_grid"))
