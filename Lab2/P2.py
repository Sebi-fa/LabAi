nota = int(input("Introdu o nota: "))

note_valide = list(range(1, 11))

while nota not in note_valide:
    print("Nota invalida! Introdu o valoare intre 1 si 10.")
    nota = int(input("Reintrodu o nota: "))

if nota <= 4:
    print("Reexaminare")
elif nota <= 6:
    print("Suficient")
elif nota <= 8:
    print("Bine")
elif nota <= 10:
    print("Excelent")