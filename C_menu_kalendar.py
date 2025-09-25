komanda = input("Komanda: ").lower().strip()

match komanda:
    case "info" | "help":
        print("Laboratori i Python — Klasa 12 TIK")
    case "ndihme":
        print("Përdor komandat: info, ndihme, dalje")
    case "dalje":
        print("Dalje nga sistemi...")
    case _:
        print("Komandë e panjohur!")

dita = int(input("Dita (1-7): "))
match dita:
    case 1:
        print("E hënë")
    case 2:
        print("E martë")
    case 3:
        print("E mërkurë")
    case 4:
        print("E enjte")
    case 5:
        print("E premte")
    case 6:
        print("E shtunë")
    case 7:
        print("E diel")
    case _:
        print("Vlerë e pavlefshme për ditën!")
