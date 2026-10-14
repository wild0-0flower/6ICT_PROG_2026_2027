artikelen = { 
    "appels": 1.50,
    "nananen": 0.75,
    "brood": 2.30,
    "melk": 1.20,
    "eieren": 2.00,
    "kaas": 3.50,
    "kip": 5.75,
    "tomaten": 1.00,
    "aardappelen": 0.80,
    "ontbijtgranen": 3.25
}
aantal_gekocht = 0
totale_prijs = 0.0

while True:
    keuze = input("Welk artikel wilt u kopen: ")
    if keuze == "STOP":
        break
    if keuze in artikelen:
        print(f"{keuze} toegevoegd.")
        aantal_gekocht = aantal_gekocht + 1
        totale_prijs = totale_prijs + artikelen[keuze]
    else:
        print(f"{keuze} bestaat niet.")
print(f"U heeft {aantal_gekocht} artikelen gekocht. Deze kosten samen {totale_prijs} euro.")