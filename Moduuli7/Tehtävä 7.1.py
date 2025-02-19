vuodenajat = {
    "Talvi": (12, 1, 2),
    "Kevät": (3, 4, 5),
    "Kesä": (6, 7, 8),
    "Syksy": (9, 10, 11)
}
kuukaudet_nimet = {
    1: "Tammikuu", 2: "Helmikuu", 3: "Maaliskuu", 4: "Huhtikuu",
    5: "Toukokuu", 6: "Kesäkuu", 7: "Heinäkuu", 8: "Elokuu",
    9: "Syyskuu", 10: "Lokakuu", 11: "Marraskuu", 12: "Joulukuu"
}
kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    kuukauden_nimi = kuukaudet_nimet[kuukausi]
    for vuodenaika, kuukaudet in vuodenajat.items():
        if kuukausi in kuukaudet:
            print(f"{kuukauden_nimi} ({kuukausi}) kuuluu vuodenaikaan {vuodenaika}.")
            break
else:
    print("Virhe: Anna numero väliltä 1-12.")
