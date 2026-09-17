# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Niveau 1
# geg_sleutel = input("Welk soort fruit zoek je: ")
# print(fruitmand[geg_sleutel])
# print(f"Er is {fruitmand[geg_sleutel]} {geg_sleutel} in de fruitmand ")
# Niveau 2
geg_sleutel = input("Welk soort fruit zoek je: ")
if geg_sleutel in fruitmand:
    print(f"Er is {fruitmand[geg_sleutel]} {geg_sleutel} in de fruitmand ")
else:
    print("Zit niet in de fruitmand")
