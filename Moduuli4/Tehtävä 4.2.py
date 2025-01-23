
while True:
    tuumat = float(input("Anna tuumien määrä: "))
    if tuumat < 0:
        break
    print(f"{tuumat} tuumaa on {tuumat * 2.54:.2f} cm")
