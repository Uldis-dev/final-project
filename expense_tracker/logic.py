def sum_total(expenses):
    """
    Aprēķina kopējo summu no visiem izdevumu ierakstiem.
    """
    total = 0.0
    for expense in expenses:
        # Piekļūstam summai, izmantojot atslēgu "amount"
        total += expense["amount"]
    return total

def sum_by_category(expenses):
    """
    Sagatavo kopsavilkumu par izdevumiem katrā kategorijā.
    Atgriež vārdnīcu, piemēram: {"Ēdiens": 25.0, "Transports": 3.4}
    """
    summary = {}
    
    for expense in expenses:
        cat = expense["category"]
        amount = expense["amount"]
        
        if cat in summary:
            summary[cat] += amount
        else:
            summary[cat] = amount
            
    return summary

if __name__ == "__main__":
    # 1. Izveidojam testa datus (sarakstu ar vārdnīcām)
    test_expenses = [
        {"date": "2024-05-01", "amount": 10.00, "category": "Ēdiens", "description": "Picas"},
        {"date": "2024-05-02", "amount": 25.50, "category": "Transports", "description": "Degviela"},
        {"date": "2024-05-03", "amount": 5.00, "category": "Izklaide", "description": "Kino"},
        {"date": "2024-05-04", "amount": 15.00, "category": "Ēdiens", "description": "Pusdienas"}
    ]

    # 2. Izsaucam summēšanas funkciju un saglabājam rezultātu
    result = sum_total(test_expenses)

    # 3. Izvadām summēsanas funkcijas rezultātu
    print("--- Pašpārbaudes tests funkcijai sum_total ---")
    print(f"Testa dati: 10.00 + 25.50 + 5.00 + 15.00")
    print(f"Gaidāmais rezultāts: 55.5")
    print(f"Faktiskais rezultāts: {result}")

    # 4. summēšanas rezultāta pārbaude
    if result == 55.5:
        print("✅ Tests veiksmīgs!")
    else:
        print("❌ Tests neizdevās. Pārbaudiet funkcijas loģiku.")

    # 5. Izsaucam summēšanas pa kategorijām funkciju un saglabājam rezultātu
    category_result = sum_by_category(test_expenses)
    # Gaidāmie rezultāti: Ēdiens (10+15=25), Transports (25.5), Izklaide (5)
    expected_categories = {"Ēdiens": 25.00, "Transports": 25.50, "Izklaide": 5.00}

    # 6. Izvadām summēsanas pa kategorijām funkcijas rezultātu
    print(f"\nFunkcija: sum_by_category")
    print(f"Gaidāmais: {expected_categories}")
    print(f"Faktiskais: {category_result}")

    # 7. summēšanas pa kategorijām rezultāta pārbaude
    if category_result == expected_categories:
        print("✅ sum_by_category tests veiksmīgs!")
    else:
        print("❌ sum_by_category tests neizdevās!")        