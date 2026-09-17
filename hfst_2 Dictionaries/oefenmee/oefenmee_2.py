# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Niveau 1
# fruit = "banaan"
# print(fruitmand[fruit])
# Niveau 2
# nieuw_fruit  = "mango"
# nieuw_aantal = 1
# fruitmand[nieuw_fruit] = nieuw_aantal
# print(fruitmand)
# Niveau 3
# fruit = "banaan"
# nieuw_aantal = 8
# fruitmand[fruit] = nieuw_aantal
# print(fruitmand)
# Niveau 4
# fruit = "kers"
# verlaag_met = 43
# fruitmand[fruit] = fruitmand[fruit] - verlaag_met
# print(fruitmand)
terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)
