nimet = set()

while True:
    lisäys = input("Lisää joukkoon nimi: ")
    if lisäys == "":
        break
    if lisäys in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(lisäys)
print(f"tässä listan sisältö {nimet}")
