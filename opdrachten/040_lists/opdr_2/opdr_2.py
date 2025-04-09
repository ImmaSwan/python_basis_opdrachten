# Opdracht 2 lists
# Naam student:sven
# Groep:IT2B


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

print (f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info['rijn'][1].capitalize()}")
print (f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info['nijl'][2].capitalize()}")
print (f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info['maas'][0].capitalize()}")