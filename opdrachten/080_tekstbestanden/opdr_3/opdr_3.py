# Opdracht 3 Tekst opslaan
# Naam student:sven van hierden
# Groep:IT2B

def encrypt(tekst):
    encrypted_text = ""

    for char in tekst:
        # Encrypt alleen letters, spaties en leestekens blijven hetzelfde
        if char.isalpha():
            # Bepaal de verschuiving voor kleine en grote letters
            start = ord('a') if char.islower() else ord('A')
            # Verschuif de letter 5 posities
            shifted_char = chr(start + (ord(char) - start + 5) % 26)
            encrypted_text += shifted_char
        else:
            # Voeg niet-lettertekens direct toe zonder encryptie
            encrypted_text += char

    return encrypted_text


# Vraag de gebruiker om de tekst die ze willen encrypten
tekst = input("Geef de tekst die je wilt encrypten..\n")

# Encrypt de tekst
encrypted_text = encrypt(tekst)

# Toon de geëncrypteerde tekst
print("\nEncrypted tekst:")
print(encrypted_text)

