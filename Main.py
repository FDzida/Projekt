samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for znak in veta:
    if not znak.isalpha():
        continue

    znak_lower = znak.lower()

    if znak_lower in samohlasky:
        vysledky["samohlasky"] += 1
    else:
        vysledky["souhlasky"] += 1

print(vysledky)