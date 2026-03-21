cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor"]

comentariu = input("Introduceți un comentariu: ")

comentariu_mic = comentariu.lower()

gasit_pozitiv = False
gasit_negativ = False

for cuvant in cuvinte_pozitive:
    if cuvant in comentariu_mic:
        gasit_pozitiv = True

for cuvant in cuvinte_negative:
    if cuvant in comentariu_mic:
        gasit_negativ = True

if gasit_pozitiv and gasit_negativ:
    print("Comentariu mixt — conține atât cuvinte pozitive cât și negative!")
elif gasit_pozitiv:
    print("Comentariu pozitiv!")
elif gasit_negativ:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")
