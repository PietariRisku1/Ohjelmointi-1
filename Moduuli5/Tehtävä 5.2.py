luvut = []

while True:
    syote = input("Syötä lukuja (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        number = int(syote)
        luvut.append(number)
    except ValueError:
        print("Syötteen täytyy olla luku. Yritä uudelleen.")

luvut.sort(reverse=True)
suurimmat_viisi = luvut[:5]
print("Viisi suurinta lukua ovat:", suurimmat_viisi)