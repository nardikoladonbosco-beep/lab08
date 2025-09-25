kategori = input("Kategori: ").lower().strip()
sasia = int(input("Sasia: "))
karte = input("Ke karte studenti? (po/jo): ").lower().strip()

match kategori:
    case "supa":
        cmimi_njesi = 120
    case "sallate":
        cmimi_njesi = 150
    case "pasta":
        cmimi_njesi = 220
    case "embelsire":
        cmimi_njesi = 180
    case _:
        print("Kategori e pavlefshme!")
        exit()

nentotal = cmimi_njesi * sasia
zbritje = 0

if karte == "po":
    zbritje += 0.10
if sasia >= 5:
    zbritje += 0.05

vlere_zbritje = nentotal * zbritje
pas_zbritjes = nentotal - vlere_zbritje

# Shtyje më tej: kupon festiv
if pas_zbritjes >= 1000:
    kupon_festiv = 0.03
    vlere_kupon = pas_zbritjes * kupon_festiv
    pas_zbritjes -= vlere_kupon
    zbritje += kupon_festiv
    vlere_zbritje += vlere_kupon

print("\n------------------------------")
print("Artikulli:", kategori, f"({cmimi_njesi} Lek)")
print("Sasia:", sasia)
print("Zbritje totale:", str(round(zbritje * 100, 2)) + "%", "(Vlera:", round(vlere_zbritje, 2), "Lek)")
print("Nën-total:", round(nentotal, 2), "Lek")
print("Totali:", round(pas_zbritjes, 2), "Lek")
