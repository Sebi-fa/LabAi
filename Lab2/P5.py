import random

print("Alege 6 numere între 1 și 49.")

numere_valide = list(range(1, 50))
numere_alese = []

for i in range(1, 7):
    numar = int(input(f"Numărul {i}: "))

    while numar not in numere_valide or numar in numere_alese:
        if numar not in numere_valide:
            print("Număr invalid! Alege un număr între 1 și 49.")
        else:
            print("Număr deja ales! Alege un număr diferit.")
        numar = int(input(f"Numărul {i}: "))

    numere_alese.append(numar)

numere_extrase = random.sample(numere_valide, 6)

ghicite = [n for n in numere_alese if n in numere_extrase]
numar_ghicite = len(ghicite)

print(f"\nNumere extrase: {numere_extrase}")
print(f"Ai ghicit {numar_ghicite} numere: {sorted(ghicite)}")

if numar_ghicite == 6:
    print("JACKPOT! Ai câștigat marele premiu!")
elif numar_ghicite == 5:
    print("Felicitări! Ai câștigat premiul I!")
elif numar_ghicite == 4:
    print("Felicitări! Ai câștigat un premiu mare!")
elif numar_ghicite == 3:
    print("Felicitări! Ai câștigat un premiu mic!")
elif numar_ghicite == 2:
    print("Aproape! Ai câștigat o consolare.")
else:
    print("Nicio potrivire. Mai încearcă!")