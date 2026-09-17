# nummers = ["+32 470 998301", "+32 483 313220", "+32 453 231456"]
# namen = ["Jan", "Piet", "Kapper Korneel"]
# geg_naam = input("Geef een naam: ")
# for index, naam in enumerate(namen):
#     if geg_naam == naam:
#         print(nummers[index])
telefoonboek = {"Jan": "+32 670 98680",
                "Piet": "+32 458 26970",
                "Kapper Korneel": "+32 345 26789"}
naam = input("geef naam:")
if naam in telefoonboek:
    print("Naam staat er in")
