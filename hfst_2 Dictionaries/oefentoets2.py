voorraad = {
    "burgers": 12,
    "loempias": 8,
    "frikandellen": 5
}
 
while True:
    snack = input("welke snack wil je: ")
 
    if snack == "stop":
        for snack,aantal in voorraad.items():
            print(snack,":",aantal)
        break
   
 
    if snack in voorraad:
        aantal = int(input("hoeveel wil je er verkopen(neg getal)/verkopen(pos getal): "))
        if (voorraad[snack] + aantal) < 0:
            print(f"fout, er zijn maar {voorraad[snack]} {snack} beschikbaar,voorraad niet gewijzigd")
        else:
            voorraad[snack] = voorraad[snack] + aantal
            print(snack,voorraad[snack])
 
    elif snack not in voorraad:
        aantal = int(input("hoeveel wil je er verkopen(neg getal)/kopen(pos getal):"))
        if aantal < 0:
            print("kan niet verkopen,aantal moet groter als 0 zijn")
        else:
            voorraad[snack] = aantal
            print(snack,aantal)
 