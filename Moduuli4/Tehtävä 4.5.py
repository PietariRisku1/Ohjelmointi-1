oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 2 # 5: oikea arvo 2: koodin testaamisen nopeuden vuoksi

while True:

    arvattu_kayttajatunnus = input("Käyttäjätunnus: ")
    arvattu_salasana = input("Salasana: ")


    if arvattu_kayttajatunnus == oikea_kayttajatunnus and arvattu_salasana == oikea_salasana:
        print("Tervetuloa")
        break

    else:
        yritykset -= 1
        print("yritä uudelleen")
        if yritykset == 0:
            print("Pääsy evätty.")
            break
