dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]
while True:
    rij = int(input("Geef een rij op: "))
    rij = rij - 1
    if rij not in dambord_2D:
        print("bestaat niet")
        break
    kolom = int(input("Geef een kolom op: "))
    kolom = kolom - 1
    if kolom not in dambord_2D:
        print("bestaat niet")
        break
    plaats = dambord_2D[rij][kolom]
    print(f"Op deze index staat {plaats}")
    #werkt niet