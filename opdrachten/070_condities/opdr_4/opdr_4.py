# Opdracht 4 condities
# Naam student: Sven van Hierden
# Groep:IT2B

# Beschikbare toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van de namen van de toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een topping te kiezen
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze in de lijst met beschikbare toppings zit
gevonden = False
for topping, prijs in toppings:
    if keuze.lower() == topping.lower():
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")