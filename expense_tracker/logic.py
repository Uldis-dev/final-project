def sum_total(expenses):
    """
    Aprēķina kopējo summu no visiem izdevumu ierakstiem.
    """
    total = 0.0
    for expense in expenses:
        # Piekļūstam summai, izmantojot atslēgu "amount"
        total += expense["amount"]
    return total


if __name__ == "__main__":
    # 1. Izveidojam testa datus (sarakstu ar vārdnīcām)
    test_expenses = [
        {"date": "2024-05-01", "amount": 10.00, "category": "Ēdiens", "description": "Picas"},
        {"date": "2024-05-02", "amount": 25.50, "category": "Transports", "description": "Degviela"},
        {"date": "2024-05-03", "amount": 5.00, "category": "Izklaide", "description": "Kino"}
    ]

    # 2. Izsaucam funkciju un saglabājam rezultātu
    result = sum_total(test_expenses)

    # 3. Izvadām rezultātu pārbaudei
    print("--- Pašpārbaudes tests funkcijai sum_total ---")
    print(f"Testa dati: 10.00 + 25.50 + 5.00")
    print(f"Gaidāmais rezultāts: 40.5")
    print(f"Faktiskais rezultāts: {result}")

    # 4. Automātiska pārbaude (pēc izvēles)
    if result == 40.5:
        print("✅ Tests veiksmīgs!")
    else:
        print("❌ Tests neizdevās. Pārbaudiet funkcijas loģiku.")