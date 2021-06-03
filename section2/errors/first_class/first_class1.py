from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


champs = [
    {"name": "Le Blanc", "K/D/A": "2/1/6"},
    {"name": "Blitz", "K/D/A": "1/5/18"},
    {"name": "Lux", "K/D/A": "11/3/8"},
]

"""
def get_champ_name(champ):
    return champ["name"]
"""

print(search(champs, "Lux", itemgetter("name")))    
#get_champ_name
#lambda champs: champs["name"]
