# Opdracht 3 condities
# Naam student:Sven van Hierden
# Groep:IT2B

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de gebruiker
gebruiker_leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))

# Bepaal de groep en de korting
for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= gebruiker_leeftijd <= max_leeftijd:
        groep_naam = groep
        korting = kortings_percentages[groep]
        break

# Bereken de prijs na de korting
korting_bedrag = normale_toegangsprijs * (korting / 100)
prijs_na_korting = normale_toegangsprijs - korting_bedrag

# Toon de resultaten
print(f"U behoort tot de groep {groep_naam}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {prijs_na_korting:.2f}")