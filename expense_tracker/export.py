import csv

def export_to_csv(expenses, filename="expenses_export.csv"):
    if not expenses:
        return False
    
    # Definējam kolonnu nosaukumus (atslēgas no taviem vārdnīcas ierakstiem)
    fieldnames = ['date', 'category', 'description', 'amount']
    
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
    return True