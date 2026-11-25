""" Oefening 2 (   / 3)
Onderstaande structuur geeft per persoon het aantal gemaakte doelpunt over 5 wedstrijden.
Print wie gemiddeld de meeste doelpunten heeft gemaakt, en hoeveel er dit waren.
Print wie gemiddeld de minste doelpunten heeft gemaakt, en hoeveel er dit waren.
De code moet blijven werken, ook als er later meer personen bijkomen.

Voor de start-datastructuur is dit het correcte antwoord.
    Meest: Sarah (2.6 doelpunten per match)
    Minst: Kiana (1.2 doelpunten per match)

"""

sport_uitslagen = {
    'Emma': [2, 3, 1, 4, 2],  # Aantal doelpunten per wedstrijd
    'Liam': [1, 2, 1, 3, 0],
    'Noah': [0, 1, 4, 1, 3],
    'Sarah': [3, 3, 4, 2, 1],
    'Kiana': [1, 0, 2, 1, 2],
    'Lucas': [2, 1, 3, 1, 0]
}
meeste_punten = 0
minste_punten = 100
for nummers,leden in enumerate(sport_uitslagen):
  max = sport_uitslagen[leden][0] + sport_uitslagen[leden][1] + sport_uitslagen[leden][2] + sport_uitslagen[leden][3] + sport_uitslagen[leden][4]
  gemm = max / 5
  if gemm < minste_punten:
    minste_punten = gemm
    slechtste_persoon = leden
  elif gemm > meeste_punten:
    meeste_punten = gemm
    beste_persoon = leden
print(f"Meest: {beste_persoon} ({meeste_punten} doelpunten per match)")
print(f"Minst: {slechtste_persoon} ({minste_punten} doelpunten per match)")