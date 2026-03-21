import random

numar = random.randint(1, 50)
contor=0

print("Am ales numarul")


while True:
    ghicire = int(input("ghiceste un numar intre 1-50= "))
    contor +=1

    if ghicire < numar:
        print("numarul este mai mare")

    elif ghicire > numar:
        print("numarul este mai mic")

    else:
        print("ai ghicit")
        print(f"ai ghicit din {contor} incercari")