deelnemers = ["Lucas", "Emma", "Jan", "Piet", "Maud"]

deelnemers_talen = {    
    "Lucas": "python",    
    "Piet": "assembly",    
    "Maud": "ruby"
}

for naam in deelnemers:
    if naam in deelnemers_talen:
        print(f"Dag {naam}, dankjewel voor de poll in te vullen.")
    else:
        print(f"Dag {naam}, gelieve de poll in te vullen.")
        taal = input("Wat is je favoriete taal: ")
        if taal != "":
            deelnemers_talen[naam] = taal

print("Antwoorden op de vraag 'favoriete taal'...")
for naam, taal in deelnemers_talen.items():
    print(f" - {naam}: {taal}")

