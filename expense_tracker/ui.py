from logic import sum_total
from datetime import datetime

def get_new_expense(categories):
    """
    Pieprasa lietotājam ievadīt datus par jaunu izdevumu.
    """
    # 1. Iegūstam šodienas datumu kā tekstu pareizā formātā
    today_str = datetime.now().strftime("%Y-%m-%d")

    print("\n--- PIEVIENOT JAUNU IZDEVUMU ---")
    try:
        date_input = input(f"Datums (YYYY-MM-DD) [{today_str}]: ")
        if date_input == "":    #ja lietotājs neievada datumu, tiek paņemts šodienas datums
            date = today_str
        else:
            date = date_input
        
        print("Kategorija: ", end="")
        for index, category in enumerate(categories, start=1):
            print(f"{index}) {category} ", end="")
        print()
        #category = input("Izvēlies (1-7): ")
        category_nr_input = int(input(f"Izvēlies numuru (1-{len(categories)}): "))

        if 1 <= category_nr_input <= len(categories):
            # No numura (piem. 1) iegūstam nosaukumu (indekss 0)
            category_name = categories[category_nr_input - 1]
        else:
            print("Kļūda: Nepareizs kategorijas numurs!")
            return None

        amount = float(input("Summa (EUR): "))
        description = input("Apraksts: ")

        return {
            "date": date,
            "amount": amount,
            "category": category_name,
            "description": description
        }
    except ValueError:
        print("Kļūda: Summai jābūt skaitlim!")
        return None
    

def display_expenses(expenses):
    if not expenses:
        print("\nSaraksts ir tukšs!")
        return

    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<15} {'Apraksts'}")
    print("-" * 60)
    
    for exp in expenses:
        # Pievienojam EUR simbolu un noformatējam decimāldaļas
        amount_str = f"{exp['amount']:>7.2f} EUR"
        print(f"{exp['date']:<12} {amount_str} {exp['category']:<15} {exp['description']}")
    
    print("-" * 60)

    # Šeit pievienojam kopsummas aprēķinu un izvadi
    total = sum_total(expenses)
    count = len(expenses)
    
    print(f"Kopā: {total:>9.2f} EUR ({count} ieraksti)")
    print("-" * 60)    