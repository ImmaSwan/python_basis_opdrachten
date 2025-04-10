# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

# my_modules/csv.py

def lijst_naar_csv(gegevens_lijst):
    return ",".join(str(item) for item in gegevens_lijst)

from my_modules import csv

# Lijst van personen als dictionaries
personen = [
    {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Den Haag"},
    {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Delft"},
    {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Utrecht"},
    {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Drachten"},
]

# Filterfunctie
def filter(lijst, veld, waarde):
    for persoon in lijst:
        if persoon[veld].lower().startswith(waarde.lower()):
            print(f"{persoon['voornaam']} {persoon['achternaam']}")

# Voorbeeldtests:
print("Filter op voornaam 'ja':")
filter(personen, "voornaam", "ja")

print("\nFilter op voornaam 'Pie':")
filter(personen, "voornaam", "Pie")

print("\nFilter op plaats 'd':")
filter(personen, "plaats", "d")