

while True:
    syote = input("Syötä lukuja (tyhjä lopettaa): ")

    if syote == "":
        break

    try:
        syote = int(syote)
    except ValueError:
        print("Syötteen täytyy olla numero.")
        continue


    if syote < 2:
        print("Syöte ei ole alkuluku.")
    else:
        on_alkuluku = True
        for i in range(2, syote):
            if syote % i == 0:
                on_alkuluku = False
                break

        if on_alkuluku:
            print("Syöte on alkuluku.")
        else:
            print("Syöte ei ole alkuluku.")


