suorakulmionkanta_string = input("Anna suorakulmion kanta: ")
suorakulmionkorkeus_string = input("Anna suorakulmion korkeus: ")

kanta = float(suorakulmionkanta_string)
korkeus = float(suorakulmionkorkeus_string)

piiri = 2 * (kanta + korkeus)
pintala = kanta * korkeus

print(f"Suorakulmion piiri = {piiri}, Suorakulmion pinta-ala = {pintala}")


