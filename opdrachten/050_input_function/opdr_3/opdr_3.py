# Opdracht 3 input functie
# Naam student:Sven van hierden
# Groep:IT2B

# Hier komt je code...

invoer = "wit, zwart, rood, roze, blauw:\n"

objecten_lijst = [item.strip() for item in invoer.split(",")]

objecten_lijst.sort(reverse=True)

print(objecten_lijst)