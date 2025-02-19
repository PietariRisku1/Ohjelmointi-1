import random

nopat = int(input("Kuinka monta noppaa heitetään: "))
summa = 0

for i in range(nopat):
    heitto = random.randint(1,6)
    summa += heitto

print(f"Noppien silmälukujen summa on : {summa}")
