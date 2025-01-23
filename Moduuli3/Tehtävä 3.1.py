kuhanpituus= int(input("Kuhan pituus (cm): "))
if kuhanpituus >=37:
    print("Onnittelut saaliista!")
else:
    puuttuvapituus = 37- kuhanpituus
    print(f"kuha ei ole tarpeeksi suuri, se on {puuttuvapituus}cm lyhyempi mitä vaaditaan")