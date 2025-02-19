import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    heitto = heita_noppaa()
    print(f"Heitto: {heitto}")
    if heitto == 6:
        print("Kutonen tuli, lopetetaan!")
        break


