# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

# Genereer een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)

# Vraag de gebruiker om te raden
aantal_pogingen = 0
geraden_getal = None

print("Raad mijn geheime getal")

# Blijf vragen totdat de gebruiker het juiste getal raadt
while geraden_getal != geheim_getal:
    # Vraag de gebruiker om een getal in te voeren
    geraden_getal = int(input())
    aantal_pogingen += 1

    # Geef feedback of het geraden getal te hoog of te laag is
    if geraden_getal < geheim_getal:
        print("hoger")
    elif geraden_getal > geheim_getal:
        print("lager")

# Als het juiste getal is geraden, geef een bericht met het aantal pogingen
print(f"Je hebt het getal geraden, het is {geheim_getal}!")
print(f"Je hebt het in {aantal_pogingen} keer gedaan")