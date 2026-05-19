def is_valid_date(text):
    """
	Pārbauda vai ievadītais teksts atbilst datuma formātam YYYY-MM-DD 
	
	Args:
	text(str): Apstrādājamā teksta virkne - datums
	
	Returns:
	bool: True/False

	Example:
	>>> is_valid_date('2026-26-aprīlis')
	False
	>>> is_valid_date('26.04.2026')
	False
	>>> is_valid_date('2026-04-26')
	True
    """

    if not isinstance(text, str) or len(text) != 10:     # Pārbaude, vai virkne ir teksts un tieši 10 simbolus garš
        return False
    
    parts = text.split("-")     # Sadalām pa domuzīmēm: ['2024', '12', '31']
    if len(parts) != 3:         # pārbaudām, vai ir 3 daļas - gads, mēnesis, datums
        return False
        
    
    for part in parts: # Pārbaudām katru daļu atsevišķi, vai ir skaitlis
        if not part.isdigit(): # Ja kaut viena daļa nav skaitlis, viss datums ir nederīgs            
            return False
        
    # Papildu loģiskā pārbaude reāliem skaitļiem
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False        
        
    return True     # Ja izietas visas iepriekšējās pārbaudes, tad datums ir derīgs


def is_valid_category(choice, max_categories):
    """
    Pārbauda, vai lietotāja izvēle ir derīgs kategorijas numurs.
    Strādā gan ar tekstu (str), gan ar veseliem skaitļiem (int).
    """
    # Ja ievade jau ir skaitlis, pārbaudām tikai diapazonu
    if isinstance(choice, int):
        return 1 <= choice <= max_categories
        
    # Ja tas ir teksts, vispirms pārbaudām, vai tie ir cipari
    if isinstance(choice, str):
        if not choice.isdigit():
            return False
        choice_num = int(choice)
        return 1 <= choice_num <= max_categories
        
    return False

def is_valid_amount(text_str):
    """
    Mēģina pārveidot tekstu par float summu, aizvietojot komatus ar punktiem.
    Atgriež float vērtību, ja viss kārtībā, vai None, ja dati ir nederīgi.
    """
    try:
        # Noņemam atstarpes un aizvietojam Eiropas komatu ar programmēšanas punktu
        cleaned_text = text_str.strip().replace(",", ".")
        amount = float(cleaned_text)
        
        # Pārbaudām biznesa loģiku: summai jābūt pozitīvai
        if amount > 0:
            return amount
        return None
        
    except ValueError:
        # Ja tekstā bija burti un float() sabojājās
        return None
    
    
def is_valid_month_choice(choice_str, max_months):
    """
    Pārbauda, vai lietotāja ievadītā mēneša izvēle ir derīgs skaitlis.
    Atgriež True, ja ir derīgs, pretējā gadījumā False.
    """
    if not choice_str.isdigit():
        return False
    
    choice_num = int(choice_str)
    return 1 <= choice_num <= max_months    