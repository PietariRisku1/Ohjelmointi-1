lentoasemat = {
    "EFHK": "Helsinki-Vantaa",
    "EFET": "Enontekiön lentoasema",
    "EFIV": "Ivalon lentoasema",
}

while True:
    print("1 - Syötä uusi ICAO koodi")
    print("2 - Etsi lentoasemien tietoja")
    print("3 - Lopeta haku")

    valinta = int(input("Anna valinta, 1, 2 tai 3: "))

    if valinta == 1:
        icao = input("Anna lentokentän ICAO koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("ICAO koodia ei löytynyt.")

    elif valinta == 2:
        icao = input("Anna ICAO koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
            if icao.length == 4:

        else:
            print("ICAO koodia ei löytynyt.")

    elif valinta == 3:
        print("Toiminto lopetetaan.")
        break

    else:
        print("Väärä valinta, kokeile uudelleen.")