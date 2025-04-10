# Opdracht 3 input functie
# Naam student:sven van hierden
# Groep:IT2B

# Hier komt je code...

# Lijst van pizza's
pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_lijst.sort()
print(pizza_lijst)

# Voeg een pizza naar keuze toe
pizza_lijst.append('yo-favorito')
print(pizza_lijst)

# Verwijder de pizza die je het minst lekker vindt
pizza_lijst.remove('olivio')
print(pizza_lijst)

# Print de eerste 3 pizza's uit de lijst
print(pizza_lijst[:3])

# Print alleen de middelste pizza uit de lijst
middle_index = len(pizza_lijst) // 2
print([pizza_lijst[middle_index]])

# Print de laatste 3 pizza's uit de lijst
print(pizza_lijst[-3:])