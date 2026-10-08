# Maak voor deze oefen mee gebruik van onderstaande dictionary-structuur.
landen_feiten = {
    'Frankrijk': {
        'hoofdstad': 'Parijs',
        'bevolking': 67348000,
        'taal': 'Frans',
    },
    'Belgi?': {
        'hoofdstad': 'Brussel',
        'bevolking': 11563000,
        'taal': ['Nederlands', 'Frans', 'Duits'],
    },
    'Duitsland': {
        'bevolking': 83190556,
        'taal': 'Duits',
    }
}
for land, info in landen_feiten.items():
    if "hoofdstad" in info:
        print(f"{land}: {info['hoofdstad']}")