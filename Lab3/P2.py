def genereaza_factura(nume_client, **kwargs):
    print(f"--- Factura pentru: {nume_client} ---")
    total = 0
    for produs, pret in kwargs.items():
        print(f"  {produs}: {pret:.2f} RON")
        total += pret
    print(f"TOTAL: {total:.2f} RON")
    print("-" * 30)

genereaza_factura(
    "Faraon Sebastian",
    Laptop=3500.00,
    Mouse=150.00,
    Tastatura=250.00
)