from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category, get_available_months, filter_by_month
from ui import wait_for_user, show_menu, get_new_expense, display_expenses, display_category_expenses, ask_month_selection, clear_screen

CATEGORIES = ["Ēdiens", "Transports", "Izklaide",
    "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

def main():
    """Galvenā programmas cilpa/cikls."""
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":   # Pievienot izdevumu
            # 2. Iegūstam jauno izdevumu no ui.py
            new_expense = get_new_expense(CATEGORIES)

            # 3. Pārbaudām, vai lietotājs neanulēja ievadi (ja funkcija atgriež None)
            if new_expense:
                expenses.append(new_expense) # Pievienojam sarakstam atmiņā
                save_expenses(expenses)      # SAGLABĀJAM JSON failā uzreiz
                print("✅  Izdevums veiksmīgi saglabāts!")

        if choice == "2":   # Parādīt izdevumus
            display_expenses(expenses)  
            wait_for_user()    

        if choice == "3":   # Filtrēt pēc mēneša
            # 1. Loģikas modulis atrod pieejamos mēnešus
            available_months = get_available_months(expenses)
            
            # 2. UI modulis nodarbojas ar parādīšanu un izvēli
            selected_month = ask_month_selection(available_months)
            
            if selected_month:
                # 3. Loģikas modulis nofiltrē datus
                filtered_data = filter_by_month(expenses, selected_month)
                
                # 4. UI modulis parāda rezultātus
                print(f"--- Izdevumi mēnesī: {selected_month} ---")
                display_expenses(filtered_data, selected_month)
                wait_for_user()            

        if choice == "4":   # Kopsavilkums pa kategorijām
            # 1. Veicam aprēķinus, izmantojot loģikas moduli
            summary_data = sum_by_category(expenses)
    
            # 2. Nododam rezultātu UI modulim attēlošanai
            display_category_expenses(summary_data)
            wait_for_user()

        elif choice == "7": # Iziet
            clear_screen()
            print("Uz redzēšanos!")
            break


if __name__ == "__main__":
    main()


