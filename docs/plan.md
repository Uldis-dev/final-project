# Sākotnējais plāns 

A. Programmas apraksts
Šī būs Python komandrindas lietotne, kas palīdzēs lietotājam ērti sekot līdzi saviem tēriņiem. Lietotājs varēs reģistrēt izdevumus, sakārtot tos pa mēnešiem un redzēt kopsavilkumu par to, kur tiek tērēta nauda. Programma saglabās visus datus failā un ļaus tos eksportēt uz Excel, lai finanšu analīze būtu pavisam vienkārša.

B. Datu struktūra
•	Izdevumu ieraksti
Tiek glabāti JSON failā kā vārdnīcas (dictionary):

{
    "date": "2024-05-20",
    "amount": 15.50,
    "category": "Pārtika",
    "description": "Pusdienas kafejnīcā"
}

Izdevumi tiek glabāti kā vārdnīcas, jo 
- lasāmība: Katrai vērtībai ir atslēga (piemēram, 'amount', vai 'category'). Tas nozīmē, ka programmētājam nav jāatceras, ka summa ir otrajā ailē, bet datums pirmajā
- vienkārša datu apstrāde: Piemēram, lai saskaitītu kopējos izdevumus,  ejam cauri sarakstam un saskaitām tikai tās vērtības, kas atrodas pie atslēgas "amount".

•	Izdevumu kategorijas 
Lai nodrošinātu datu kārtību, lietotājs nevarēs izdomāt savus kategoriju nosaukumus katru reizi no jauna. Programmas sākumā tiek definēts fiksēts saraksts CATEGORIES. 
Iespējams, nākotnē, programmu var papildināt ar funkcionalitāti - lietotājam papildināt kategoriju sarakstu. Tādā gadījumā kategorijas tiktu saglabātas atsevišķā JSON failā kā saraksts:

[
    "Pārtika",
    "Transports",
    "Izklaide",
    "Mājoklis",
    "Citi",
    "Veselība"
]


C. Moduļu plāns
Projektā plānojas šādi faili

storage.py
JSON failu operācijas
- load_expenses() - nolasa izdevumus no JSON faila
- save_expenses(expenses) - saglabā izdevumus JSON failā

logic.py
Biznesa loģika
- filter_by_month
- sum_total(expenses) - aprēķina kopējo summu
- sum_by_category(expenses) - atgriež vārdnīcu, kurā pa izdevumu kategorijām sasummēti izdevumi
- get_available_months(expenses) - atgriež unikālo mēnešu sarakstu

export.py
Eksports uz CSV failu
- export_to_csv(expenses, filepath) - saglabā izdevumus CSV failā

app.py
Galvenā programma - importē funkcijas no pārējiem moduļiem un veido izvēlni darbībām ar programmu

iespejams, ka tiks izveidots modulis
validators.py
ar funkcijām, kas validē lietotāja ievadītos datus



D. Lietotāja scenāriji
•	Izdevuma pievienošana
Lietotājs izvēlas darbību 'Pievienot izdevumu'. Programma piedāvā ievadīt datumu (parāda, kāds formāts ir nepieciešams). Ja lietotājs ievada datumu nepareizā formātā, programma prasa atkārtoti ievadīt datumu, kamēr saņem derīgu. Ja lietotājs datumu neievada, programma paņem šodienas datumu. Pēc tam programma piedāvā izvēlēties vienu no izdevumu kategorijas numuru (kategorijas ir iepriekš nodefinētas, lietotājs nevar tās manīt vai pievienot). Ja lietotājs ieraksta neatbilstošu numuru vai kādu tekstu, programma prasa atkartoti ievadīt kategorijas numuru. Tālāk programma prasa ievadīt izdevumu summu. Ja lietotājs ievada negatīvu skaitli, atstāj tukšumu, ieraksta tekstu, programma prasa atkārtoti ievadīt summu. Pēc tam programma prasa ievadīt izdevumu aprakstu. Ja lietotājs neieraksta aprakstu, programma šo izdevumu saglabā ar aprakstu 'Nav apraksta'.
•	Izdevuma dzēšana
Lietotājs izvēlas darbību 'Dzēst izdevumu'. Programma parāda sanumurētu sarakstu ar visiem izdevumu ierakstiem, sakārtotiem pieaugošā secībā pēc datumiem. Programma prasa, kuru izdevumu dzēst (rindas numuru). Lai atceltu dzēšanu, lietotājam jāievada 0. Ja lietotājs ievada numuru, kas atbilst izdevumu rindas numuram, programma parāda paziņojumu 'Dzēsts:' un pārējo informāciju par dzēsto izdevumu - datums, summa, kategorija, apraksts. Ja lietotājs ievada numuru, kas ir lielāks nekā rindu skaits izdevumu sarakstā, atstāj tukšumu vai ieraksta tekstu, programma prasa atkārtoti ievadīt dzēšamās rindas numuru.
•	Izdevumu filtrēšana pēc mēneša
Lietotājs izvēlas darbību 'Filtrēt pēc mēneša'. Programma izanalizē izdevumu sarakstu un parāda sanumurētu sarakstu ar pieejamajiem mēnešiem(GGGG-MM), kurus lietotājs var izvēlēties filtrēšanai. Ja lietotājs ievada numuru, kas lielāks, nekā rindu skaits pieejamo mēnešu sarakstā, atstāj tukšumu, vai ieraksta tekstu, programma prasa atkārtoti ievadīt mēneša numuru. Kad lietotājs ir ievadījis derīgu mēneša numuru, pēc kura atfiltrēt izdevumus, programa atgriež - mēnesi (GGGG-MM), sarakstu ar mēneša izdevumiem (pieaugošā secībā pēc datumiem), kopsummu eur un ierakstu skaitu.


E. Robežgadījumi
•	izdevumu fails expenses.json neeksistē
Programma pati izveido tukšu sarakstu mainīgajā, lai darbs varētu turpināties bez kļūdas ziņojuma.
•	izdevumu fails expenses.json nav nolasāms (piem., tajā ir kļūdas)
Programma informē lietotāju par bojāto failu un piedāvā sākt jaunu sarakstu.
•	lietotājs ievada negatīvu summu
Programma parāda brīdinājumu, ka summa nevar būt negatīva, un lūdz ievadīt pareizu vērtību vēlreiz.
•	lietotājs neieraksta izdevumu aprakstu
Programma automātiski piešķir noklusējuma tekstu, piemēram, 'Nav apraksta', lai ieraksts nebūtu tukšs.
•	lietotājs norāda datumu nepareizā formātā
Programma parāda pareiza formāta piemēru (GGGG-MM-DD) un lūdz ievadīt datumu atkārtoti vai piedāvā izmantot šodienas datumu.
•	lietotājs izvēlas apskatīt izdevumu sarakstu, bet tas ir tukšs
Programma izvada skaidru ziņojumu "Saraksts pašlaik ir tukšs, lūdzu, vispirms pievienojiet kādu izdevumu".