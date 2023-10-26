import csv
import csv_module as cm
import config as cg
import numpy as np
from tabulate import tabulate

new_pokemon = []


def max_value(data, col):
    highest_value = max([int(row[col]) for row in data])
    return highest_value


def list_types(listdata):
    unique_types = np.unique(listdata)
    return unique_types


def print_list(dl):
    for a, b, c in zip(dl[::3], dl[::3], dl[2::3]):
        print('{:<30}{:<30}{:<}'.format(a, b, c))


def pokemon_creator():
    column = [x[2] for x in cm.tbl_data]
    uniques = list_types(column)
    while True:
        name = input('Type in a name for you new pokemon: \n')
        check = input(
            f'Are you happy with {name.title()} as your new pokemon? [Y/N]\n')

        while check.upper() not in ['Y', 'N']:
            check = input(cg.error_message)

        if check.upper() == 'Y':
            new_pokemon.append(max_value(cm.tbl_data, 0) + 1)
            new_pokemon.append(name.title())
            break
        elif check.upper() == 'N':
            continue

    print_list(uniques)

    while True:
        type_selection = input(
            '\nUsing the list above input your selected type(s) separated by a comma(,). You can choose a maximum of 2.\n')
        select_list = type_selection.split(',')
        if len(select_list) > 2:
            print('You selected too many types!')
        elif len(select_list) < 1:
            print('Please select Pokemon type.')
        else:
            if len(select_list) == 1:
                if valid_pokemon(select_list, uniques):
                    for pokemon in select_list:
                        new_pokemon.append(pokemon.title())
                        new_pokemon.append('')
            else:
                if valid_pokemon(select_list, uniques):
                    for pokemon in select_list:
                        new_pokemon.append(pokemon.title())
            break

    user_rand = input(
        'Select from the following options:\n[1] Choose my own stats [2] Have them randomly assigned\n')
    while user_rand not in ['1', '2']:
        user_rand = input(cg.error_message + '\n')
    user_rand = int(user_rand)
    stat_max = []
    stat_headers = cm.headers[5:10]
    stat_headers.insert(0, '')
    for i in range(5, 10):
        stat_max.append(max_value(cm.tbl_data, i))
    stat_max.insert(0, 'Maximum Value:')
    if user_rand == 1:
        print(tabulate([stat_max], headers=stat_headers,
              tablefmt='fancy_grid'))
        user_stats = (
            'Input your own stats for the above stat types followed by a comma(,). Do not exceed the maximum value.\n')
        stats_list = type_selection.split(',')
    # elif user_rand == 2:


def valid_pokemon(select_list, unique):
    for x in select_list:
        x = x.strip()
        if x not in unique:
            print(f'{x} in not a valid type!')
            return False
    return True


if len(new_pokemon) == 14:
    with cm.open_pokemon_csv('w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_pokemon)


def pokemon_create_main():
    pass


pokemon_creator()
print(new_pokemon)
# # create the csv writer
# writer = csv.writer(csv_file:)
# writer.writerows(data)
