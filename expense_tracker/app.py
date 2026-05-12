from storage import load_expenses, save_expenses
from logic import sum_total
from ui import get_new_expense, display_expenses

CATEGORIES = ["Ēdiens", "Transports", "Izklaide",
    "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")
    # ... pārējās komandas ...
    return input("\nIzvēlies darbību (1-7): ")

def main():
    """Galvenā programmas cilpa/cikls."""
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            # 2. Iegūstam jauno izdevumu no ui.py
            new_expense = get_new_expense(CATEGORIES)

            # 3. Pārbaudām, vai lietotājs neanulēja ievadi (ja funkcija atgriež None)
            if new_expense:
                expenses.append(new_expense) # Pievienojam sarakstam atmiņā
                save_expenses(expenses)      # SAGLABĀJAM JSON failā uzreiz
                print("Izdevums veiksmīgi saglabāts!")

        if choice == "2":
            display_expenses(expenses)         
        elif choice == "7":
            print("Uz redzēšanos!")
            break


if __name__ == "__main__":
    main()


