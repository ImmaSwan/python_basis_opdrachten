# Opdracht 1 functies
# Naam student:sven van hierden
# Groep:IT2B


def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Maak een lijst van de naamonderdelen en filter lege strings eruit
        onderdelen = [persoon["voornaam"], persoon["tussenvoegsel"], persoon["achternaam"]]
        naam = " ".join(deel for deel in onderdelen if deel.strip() != "")
        print(naam)

# Testdata
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Functie aanroepen
volledige_naam(namen)
