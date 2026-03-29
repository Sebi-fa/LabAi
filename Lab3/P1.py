def rock_paper_scissors():
    optiuni = ["piatra", "hartie", "foarfeca"]
    castigatori = {
        ("piatra",   "foarfeca"): "Piatra bate foarfeca!",
        ("foarfeca", "hartie"):  "Foarfeca taie hartia!",
        ("hartie",   "piatra"):   "Hartia bate piatra!",
    }

    while True:
        j1 = input("Jucator 1 (piatra/hartie/foarfeca): ").lower()
        j2 = input("Jucator 2 (piatra/hartie/foarfeca): ").lower()

        if j1 not in optiuni or j2 not in optiuni:
            print("Alegere invalida! Incercati din nou.")
            continue

        print(f"\nJucator 1: {j1} | Jucator 2: {j2}")

        if j1 == j2:
            print("Egalitate!")
        elif (j1, j2) in castigatori:
            print(castigatori[(j1, j2)])
            print("Felicitari, Jucator 1!")
        else:
            print(castigatori[(j2, j1)])
            print("Felicitari, Jucator 2!")

        din_nou = input("\nDoriti un nou joc? (da/nu): ").lower()
        if din_nou != "da":
            print("La revedere!")
            break

rock_paper_scissors()