
sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ").lower()


if sukupuoli != "nainen" and sukupuoli != "mies":
    print("Virheellinen sukupuolensyöte.")
else:

    hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))



    if sukupuoli == "nainen":
        if 117 <= hemoglobiini <= 175:
            print("Hemoglobiiniarvo on normaali.")
        elif hemoglobiini < 117:
            print("Hemoglobiiniarvo on alhainen.")
        else:
            print("Hemoglobiiniarvo on korkea.")

    elif sukupuoli == "mies":
        if 134 <= hemoglobiini <= 195:
            print("Hemoglobiiniarvo on normaali.")
        elif hemoglobiini < 134:
            print("Hemoglobiiniarvo on alhainen.")
        else:
            print("Hemoglobiiniarvo on korkea.")