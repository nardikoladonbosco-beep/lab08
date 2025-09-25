n = int(input("Jep n: "))

if n > 0:
    print("Pozitiv", end="")
elif n == 0:
    print("Zero", end="")
else:
    print("Negativ", end="")

if n % 5 == 0 and n != 0:
    print(" (Sh.m i 5)")
else:
    print()
