import csv
import random
from csv_module import open_pokemon_csv

def random_pokemon():
  with open_pokemon_csv() as csvfile:
    reader = csv.reader(csvfile)
    chosen_row = random.choice(list(reader))
    print(chosen_row)
