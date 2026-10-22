import random
flashkaarten = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "auto": "car",
}
woorden = list(flashkaarten.keys())
random.shuffle(woorden)
foute_woorden = []
for woord in woorden:
    vertaling = input(f"Wat is de vertaling van {woord}: ")
    if vertaling == flashkaarten[woord]:
        print("Dit klopt!")
    else:
        print("Dit klopt niet!")
        foute_woorden.append(woord)
if len(foute_woorden) > 0:
    print("Oefen meer op deze woorden...")
    for woord in foute_woorden:
        print(f" - {woord}: {flashkaarten[woord]}")
else:
    print("Geen fouten, super gedaan!")



