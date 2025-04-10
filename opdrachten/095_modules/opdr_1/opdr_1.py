# Opdracht 1 functies
# Naam student: Sven van Hierden
# Groep:

def lijst_naar_csv(gegevens_lijst):
    """Zet een lijst om naar een CSV-string."""
    return ",".join(str(item) for item in gegevens_lijst)


from my_modules import csv

# Voorbeeldlijst
data = ["voornaam", "achternaam", "leeftijd"]

# Gebruik de functie uit je eigen module
csv_regel = csv.lijst_naar_csv(data)

print("CSV-regel:", csv_regel)