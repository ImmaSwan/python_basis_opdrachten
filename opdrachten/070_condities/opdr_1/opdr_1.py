# Opdracht 1 condities
# Naam student:sven van hierden
# Groep:IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Maak een lege lijst
lijst = []

# Vul de lijst met getallen van 1 t/m 10
for i in range(1, 11):
    lijst.append(i)

# Print alleen de getallen die groter zijn dan 4
for getal in lijst:
    if getal > 4:
        print(getal)