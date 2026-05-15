from logic import sum_total
from datetime import datetime
import os

def clear_screen():
    """
    Notīra termināla ekrānu atkarībā no operētājsistēmas.
    """
    # Windows sistēmā os.name ir 'nt', macOS/Linux tā ir 'posix'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def wait_for_user():
    """
    Aptur programmas darbību, līdz lietotājs nospiež Enter.
    """
    print("\n" * 3)
    print("─" * 70)
    input("Nospiediet [Enter], lai atgrieztos izvēlnē...")        

def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    clear_screen()
    print("\n")
    print("=" * 70)
    print("  IZDEVUMU IZSEKOTĀJS")
    print("=" * 70)
    print("    Galvenā izvēlne")      
    print("─" * 70)


    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")    
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")    
    print("6) Eksportēt CSV")            
    print("7) Iziet")

    return input("\nIzvēlies darbību (1-7): ")

def get_new_expense(categories):
    """
    Pieprasa lietotājam ievadīt datus par jaunu izdevumu.
    """
    # 1. Iegūstam šodienas datumu kā tekstu pareizā formātā
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    clear_screen()
    print("\n")
    print("=" * 70)
    print("  IZDEVUMU IZSEKOTĀJS")
    print("=" * 70)
    print("    Pievienot jaunu izdevumu")
    print("─" * 70)
    print("\n")

    try:
        date_input = input(f"Datums (YYYY-MM-DD), atstājot tukšu, tiks paņemts šodienas datums ({today_str}): ")
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
            print("      ❌ Kļūda: Nepareizs kategorijas numurs!")
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
        print("      ❌ Kļūda: Summai jābūt skaitlim!")
        return None
    

def display_expenses(expenses, filter_value=None):
    clear_screen()
    print("\n")
    print("=" * 70)
    print("  IZDEVUMU IZSEKOTĀJS")
    print("=" * 70)
    title = "    Izdevumu saraksts"
    # 2. Ja filtrs ir norādīts, pievienojam to virsrakstam iekavās
    if filter_value:
        title += f" ({filter_value})"
    print(f"{title}")
    print("─" * 70)

    if not expenses:
        print("\n      ❌ Saraksts ir tukšs!")
        return

    print(f"\n{'Datums':<18} {'Summa':<8} {'Kategorija':<15} {'Apraksts':<33}")
    print("─" * 70)
    
    for exp in expenses:
        # Pievienojam EUR simbolu un noformatējam decimāldaļas
        amount_str = f"{exp['amount']:.2f}"
        print(f"{exp['date']:<12} {amount_str:>10} EUR {exp['category']:<15} {exp['description']:<33}")
    
    print("─" * 70)

    # Šeit pievienojam kopsummas aprēķinu un izvadi
    total = sum_total(expenses)
    count = len(expenses)
    
    print(f"  {'KOPĀ:':<10} {total:>10.2f} EUR ({count} ieraksti)")
    print("─" * 70)    


def display_category_expenses(summary):
    """
    Attēlo kopsavilkumu pa kategorijām glītā formātā.
    """
    clear_screen()
    print("\n")
    print("=" * 70)
    print("  IZDEVUMU IZSEKOTĀJS")
    print("=" * 70)
    print("    Kopsavilkums pa kategorijām")
    print("─" * 70)

    if not summary:
        print("\n      ❌ Nav datu kopsavilkuma izveidei.")
        return

    print(f"\n{'Kategorija':<22} {'Summa':<10}")
    print("─" * 31)

    grand_total = 0
    
    # Ejam cauri vārdnīcas elementiem (atslēga, vērtība)
    for category, amount in summary.items():
        # :<15 norāda, ka tekstam jāaizņem 15 zīmes, līdzinot pa kreisi
        # :>10.2f norāda 10 zīmes, līdzinot pa labi, ar 2 cipariem aiz komata
        print(f"{category:<16} {amount:>10.2f} EUR")
        grand_total += amount
        
    print("─" * 31)
    print(f"  {'KOPĀ:':<14} {grand_total:>10.2f} EUR")


def ask_month_selection(months):
    """
    Parāda pieejamos mēnešus un prasa lietotājam izvēlēties vienu.
    Atgriež izvēlēto mēnesi (string) vai None.
    """
    clear_screen()
    print("\n")
    print("=" * 70)
    print("  IZDEVUMU IZSEKOTĀJS")
    print("=" * 70)
    print("    Filtrēt pēc mēneša")
    print("─" * 70)
    print("\n")


    if not months:
        print("\n     ❌ Nav pieejamu datu par mēnešiem.")
        return None

    print("      Pieejamie mēneši")
    print("─" * 30)
    
    for index, month in enumerate(months, start=1):
        print(f"{index}) {month}")

    try:
        choice = int(input(f"\nIzvēlieties numuru (1-{len(months)}): "))
        if 1 <= choice <= len(months):
            return months[choice - 1]
        else:
            print("      ❌ Kļūda: Skaitlis nav sarakstā.")
            return None
    except ValueError:
        print("      ❌ Kļūda: Lūdzu, ievadiet veselu skaitli!")
        return None    