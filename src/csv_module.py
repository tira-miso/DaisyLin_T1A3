import os

def open_pokemon_csv():

    pokemon_masterlist = "pokemonOG.csv"
    pokemon_csv_path = os.path.join(os.path.dirname(__file__), pokemon_masterlist)

    try: 
        csv_file = open(pokemon_csv_path, 'r')
        return csv_file
        
    except FileNotFoundError:
        print("File not found:", pokemon_csv_path)
        return None
    
