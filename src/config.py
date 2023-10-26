#Added error message to avoid repetitve code
menu = ("""
                  
Enter [1] to display all Pokémon.
Enter [2] to search Pokémon.
Enter [3] to get a random Pokémon.  
Enter [4] to add your own Pokémon.
                       
Enter [5] to Close Pokédex.                      

""")
error_message = 'Please enter a valid reply.'
#Declared variable in config module to avoid global requirement used in previous main.py
main_run = True
#empty list stored in config so search history can be retained when moving between funcs
search_history = []

#Installed packages:
#pip install tabulate
