# Definiramo znake in njihova kodiranja
characters = ['Č', 'Š', 'Ž', 'č', 'š', 'ž']
encodings = ['cp852', 'iso-8859-2', 'windows-1250', 'mac-croatian', 'utf-8', 'utf-16le', 'utf-16be']

# Zanka čez vsa kodiranja in izpis kodiranih vrednosti 
for encoding in encodings:
    print(f"\n{encoding.upper()}:")
    for char in characters:
        # Kodiramo znake in izračunamo binarne, decimalne in heksadecimalne reprezentacije
        encoded_char = char.encode(encoding, 'replace')
        hex_val = encoded_char.hex().upper()
        dec_val = int.from_bytes(encoded_char, 'big')
        bin_val = bin(dec_val)[2:]
        print(f"{char}: BIN({bin_val}) DEC({dec_val}) HEX({hex_val})")
