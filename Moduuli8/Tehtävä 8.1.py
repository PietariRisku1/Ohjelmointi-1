import mysql.connector


# Yhteyden muodostaminen tietokantaan
def muodosta_yhteys():
    return mysql.connector.connect(
        host="127.0.0.1",  # Tietokannan isäntä
        port=3306,  # Portti
        database="Flight_game",  # Tietokannan nimi
        user="pietarinlenovo",  # Käyttäjätunnus
        password="pietari9046",  # Salasana
        autocommit=True
    )


# Funktio, joka hakee kentän tiedot ICAO-koodin perusteella
def hae_kentta(icao_koodi):
    try:
        yhteys = muodosta_yhteys()  # Yhdistetään tietokantaan
        kursori = yhteys.cursor()  # Luodaan kursori

        # Suoritetaan SQL-kysely, joka hakee kentän nimen ja sijaintikunnan
        kysely = """
        SELECT name, municipality
        FROM airport
        WHERE ident = %s
        """
        kursori.execute(kysely, (icao_koodi,))

        # Haetaan tulokset ja tulostetaan ne
        tulos = kursori.fetchone()

        if tulos:
            print(f"Lentokentän nimi: {tulos[0]}")
            print(f"Sijaintikunta: {tulos[1]}")
        else:
            print(f"ICAO-koodilla {icao_koodi} ei löytynyt lentokenttää.")

    except mysql.connector.Error as err:
        print(f"Virhe tietokantayhteydessä: {err}")

    finally:
        if 'yhteys' in locals() and yhteys.is_connected():
            kursori.close()
            yhteys.close()


# Pääohjelma
def main():
    icao_koodi = input("Syötä ICAO-koodi: ").upper()  # Kysytään ICAO-koodia käyttäjältä
    hae_kentta(icao_koodi)  # Haetaan ja tulostetaan kentän tiedot


if __name__ == "__main__":
    main()