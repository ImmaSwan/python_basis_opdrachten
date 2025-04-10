# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Dictionary om antwoorden op te slaan
feestganger = {}

# Vragen stellen en antwoorden opslaan
for i, vraag in enumerate(vragen, 1):
    antwoord = input(f"{i}. {vraag}\n")
    if "voornaam" in vraag.lower():
        feestganger["voornaam"] = antwoord
    elif "achternaam" in vraag.lower():
        feestganger["achternaam"] = antwoord
    elif "drank" in vraag.lower():
        feestganger["drank"] = antwoord
    elif "eten" in vraag.lower():
        feestganger["eten"] = antwoord

# Antwoord bevestiging
print("\nBedankt voor het invullen!")
print("See you at the party.\n")

# Gegevens opslaan in tekstbestand
with open("feestgangers.txt", "a") as bestand:
    for key, value in feestganger.items():
        bestand.write(f"{key}: {value}\n")
    bestand.write("\n")  # lege regel tussen feestgangers
