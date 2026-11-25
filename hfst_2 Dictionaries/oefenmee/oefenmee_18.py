dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]
while True:
    rij = int(input("Geef een rij op: "))
    if rij < 0 or rij >= len(dambord_2D):
        print("bestaat niet")
        break
    kolom = int(input("Geef een kolom op: "))
    if kolom < 0 or kolom >= len(dambord_2D[rij]):
        print("bestaat niet")
        break
    plaats = dambord_2D[rij][kolom]
    print(f"Op deze index staat {plaats}")