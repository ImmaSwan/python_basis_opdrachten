# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Open het bestand waar de resultaten worden opgeslagen (bijvoorbeeld 'enquete_resultaten.txt')
with open('enquete_resultaten.txt', 'w') as bestand:
    # Loop door elke vraag
    for vraag in vragen:
        # Vraag de gebruiker om een antwoord
        antwoord = input(vraag + "\n")
        # Schrijf het antwoord naar het bestand
        bestand.write(vraag + "\n")
        bestand.write("Antwoord: " + antwoord + "\n\n")

print("De antwoorden zijn opgeslagen in 'enquete_resultaten.txt'.")