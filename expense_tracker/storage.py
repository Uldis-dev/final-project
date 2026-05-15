import os
import json

def load_expenses(expenses_file="expenses.json"):
    """
    Nolasa izdevumu sarakstu no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu.
    
    Args:
    expenses_file(str): Ceļš līdz JSON failam, kurā glabājas izdevumu saraksts.
    
    Returns:
    list: Izdevumu saraksts (saraksts ar vārdnīcām) vai [] ja fails neeksistē.

    Example:
    >>> load_expenses('neeksistejos_fails.json')
    []
    >>> load_expenses('expenses.json')
    [{
    "date": "2024-05-20",
    "amount": 15.50,
    "category": "Pārtika",
    "description": "Pusdienas kafejnīcā"
    }]
    """
    if not os.path.exists(expenses_file):
        return []   # ja fails nav, atgriež tukšu sarakstu
    
    try:
        with open(expenses_file, 'r', encoding='utf-8') as file:
            raw_expenses = json.load(file)
            # Uzreiz sakārtojam visus izdevumus pēc datuma hronoloģiskā secībā
            sorted_expenses = sorted(raw_expenses, key=lambda x: x["date"])
            return sorted_expenses  #ielasa faila saturu atmiņā
    except (json.JSONDecodeError, IOError):
        # Ja fails ir bojāts vai to nevar nolasīt, atgriežam tukšu sarakstu
        return []        
        

def save_expenses(expenses, expenses_file="expenses.json"):
    """
    Saglabā izdevumu sarakstu JSON failā, izmantojot UTF-8 kodējumu.
    
    Args:
    expenses(list): Saraksts ar vārdnīcām, ko nepieciešams saglabāt.
    expenses_file(str): Ceļš līdz JSON failam, kurā dati tiks ierakstīti.
    
    Returns:
    None: Funkcija datus tikai ieraksta failā un vērtību neatgriež.
    """    
    with open(expenses_file, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4) #pārveido json formātā    

if __name__ == "__main__":
    # Šis bloks kalpo tikai ātrai pašpārbaudei
    test_data = [{
    "date": "2024-05-20",
    "amount": 15.50,
    "category": "Pārtika",
    "description": "Pusdienas kafejnīcā"
    }]
    save_expenses(test_data, "test.json")
    print("Dati saglabāti test.json")
    print("Ielādētie dati:", load_expenses("test.json"))