pike = int(input("Pike: "))
if pike < 0 or pike > 100:
    print("Niveli: Vlerë e pavlefshme")
elif pike >= 90:
    print("Niveli: Shkëlqyeshëm")
elif pike >= 80:
    print("Niveli: Shume mire")
elif pike >= 70:
    print("Niveli: Mire")
elif pike >= 50:
    print("Niveli: Kalues")
else:
    print("Niveli: Dobët")

cmimi = float(input("Cmimi: "))
if cmimi < 100:
    print("Etiketa: I lirë")
elif cmimi < 500:
    print("Etiketa: Mesatar")
else:
    print("Etiketa: I shtrenjtë")
