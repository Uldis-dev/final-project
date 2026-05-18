from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category, get_available_months, filter_by_month, delete_expense
from ui import wait_for_user, show_menu, get_new_expense, display_expenses, display_category_expenses, ask_month_selection, clear_screen, ask_expense_to_delete, show_export_status
from export import export_to_csv

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
            available_months = get_available_months(expenses)
            selected_month = ask_month_selection(available_months)
            
            if selected_month:
                filtered_data = filter_by_month(expenses, selected_month)
                display_expenses(filtered_data, selected_month)
                wait_for_user()            

        if choice == "4":   # Kopsavilkums pa kategorijām
            summary_data = sum_by_category(expenses)
    
            display_category_expenses(summary_data)
            wait_for_user()

        if choice == "5":   # Dzēst izdevumu   
            index_to_delete = ask_expense_to_delete(expenses)
            
            if index_to_delete is not None:
                success = delete_expense(expenses, index_to_delete)
                
                if success:
                    save_expenses(expenses) 
                    print("Saraksts atjaunināts un saglabāts.")
            
            wait_for_user()        
        
        if choice == "6":   # Eksportēt CSV
            filename = "izdevumi_eksports.csv"
            success = export_to_csv(expenses, filename)
            show_export_status(success, filename)
            wait_for_user()    

        elif choice == "7": # Iziet
            clear_screen()
            print("Uz redzēšanos!")
            break


if __name__ == "__main__":
    main()


