import random

print(" Bine ai venit în Pădurea Magică! ")
print("Ai 3 etape de parcurs. Mult succes!")

inventar = []
viata = 100

print("\n--- ETAPA 1 ---")
print("Ajungi la o răscruce în pădure.")
alegere = input("Mergi la stânga sau dreapta? ")

if alegere == "stânga" or alegere == "stanga":
    print(" Un lup îți iese în cale și te zgârie!")
    viata = viata - 20
    print(f"Ai pierdut 20 de viață. Viață rămasă: {viata}")
else:
    print(" Găsești un cufăr cu o sabie magică!")
    inventar.append("sabie magică")
    print(f"Inventar: {inventar}")


print("\n--- ETAPA 2 ---")
print("Ajungi lângă un lac strălucitor.")
alegere = input("Mergi la stânga sau dreapta? ")

if alegere == "stânga" or alegere == "stanga":
    print(" O zână te vindecă!")
    viata = viata + 20
    print(f"Ai câștigat 20 de viață. Viață rămasă: {viata}")
else:
    print(" Calci într-o mlaștină și pierzi timp și energie!")
    viata = viata - 10
    print(f"Ai pierdut 10 de viață. Viață rămasă: {viata}")


print("\n--- ETAPA 3 ---")
print("Ajungi la o peșteră misterioasă.")
alegere = input("Mergi la stânga sau dreapta? ")

if alegere == "stânga" or alegere == "stanga":
    print(" Un dragon mic te atacă!")
    if "sabie magică" in inventar:
        print("Folosești sabia magică și îl alungi!")
    else:
        viata = viata - 30
        print(f"Ai pierdut 30 de viață. Viață rămasă: {viata}")
else:
    print(" Găsești o comoară cu aur și bijuterii!")
    inventar.append("aur")
    print(f"Inventar: {inventar}")


print("\n--- SFÂRȘIT ---")
print(f"Viață rămasă: {viata}")
print(f"Inventar final: {inventar}")

if viata <= 0:
    print("Ai murit în pădure. Mai încearcă!")
elif viata >= 80:
    print("Aventurier legendar!")
elif viata >= 50:
    print("Aventurier bun!")
else:
    print("Ai supraviețuit, dar abia!")