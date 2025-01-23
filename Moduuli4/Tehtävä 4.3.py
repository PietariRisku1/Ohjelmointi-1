
suurin = None
pienin = None

while True:
    syote = input("Anna luku (tyhjä syöte lopettaa): ")

    if syote == "":
        break

    try:
        luku = float(syote)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")
        continue

    if suurin is None or pienin is None:
        suurin = luku
        pienin = luku
    else:
        if luku > suurin:
            suurin = luku
        if luku < pienin:
            pienin = luku

print(f"Suurin luku on: {suurin}")
print(f"Pienin luku on: {pienin}")