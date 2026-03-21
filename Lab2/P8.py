tari_risc = ["Coreea de Nord", "Siria", "Iran"]

tranzactii = []
numar_suspecte = 0
cont_blocat = False

print("SISTEM BANCAR")
numar = int(input("Câte tranzacții vrei să introduci? "))

for i in range(1, numar + 1):
    print(f"\n-- Tranzacția {i} --")
    suma = float(input("Suma (RON): "))
    tara = input("Țara: ")

    tranzactii.append({"suma": suma, "tara": tara})

print("\nProcesăm tranzacțiile...")
print("-" * 45)

for t in tranzactii:
    suma = t["suma"]
    tara = t["tara"]

    suma_mare = suma > 10000
    tara_riscanta = tara in tari_risc

    if tara_riscanta and suma_mare:
        stare = "Frauduloasă (sumă mare + țară cu risc ridicat)"
        numar_suspecte += 1

    elif tara_riscanta:
        stare = "Frauduloasă (țară cu risc ridicat)"
        numar_suspecte += 1

    elif suma_mare:
        stare = "Suspicioasă (sumă mare)"
        numar_suspecte += 1

    else:
        stare = "Sigură"

    print(f"Tranzacție: {suma:.0f} RON din {tara} → {stare}")

    if numar_suspecte >= 3:
        cont_blocat = True
        break

print("-" * 45)

if cont_blocat:
    print(f"\n {numar_suspecte} tranzacții suspecte detectate! Cont BLOCAT.")
else:
    print(f"\n Tranzacții suspecte: {numar_suspecte}. Contul este activ.")