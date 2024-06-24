import openpyxl

# Branje decimalnih Unicode točk iz datoteke
with open("kodne_tocke.txt", "r") as file:
    code_points = file.read().strip().split(", ")

# Pretvorba decimalnih števil v heksadecimalne Unicode zapise
hex_numbers = [hex(int(decimal_number))[2:].zfill(4) for decimal_number in code_points]
unicode_characters = [f"\\u{hex_num}" for hex_num in hex_numbers]
unicode_string = "".join(unicode_characters).encode().decode('unicode-escape')

# Pisanje teh znakov v izhodno datoteko
with open("generated_text.txt", "w", encoding="utf-8") as file:
    file.write(unicode_string)

# Priprava podatkov za Excel tabelo
unique_characters = {character: [bin(ord(character)), ord(character), hex(ord(character))] for character in unicode_string}
table_header = ["Znak", "Bin", "Dec", "Hex"]
rows = [[character] + info for character, info in unique_characters.items()]

# Ustvarjanje in polnjenje Excel datoteke
wb = openpyxl.Workbook()
ws = wb.active
ws.append(table_header)
for row in rows:
    ws.append(row)

wb.save("unique_characters_codes.xlsx")
