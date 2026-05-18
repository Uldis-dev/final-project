# Projekta dokumentācija

# Izdevumu izsekotājs

Komandrindas Python lietojumprogramma personīgo izdevumu uzskaitei, hronoloģiskai analīzei un eksportam. Programma automātiski kārto izdevumus pēc datuma un nodrošina pārskatāmu datu attēlošanu.

## Uzstādīšana

Lejupielādējiet projektu un palaidiet to, izmantojot termināli:


git clone [https://github.com/Uldis-dev/final-project.git](https://github.com/Uldis-dev/final-project.git)
cd expense-tracker
python app.py

Nav nepieciešamas papildus bibliotēkas — tiek izmantoti tikai Python iebūvētie moduļi (json, csv, os). 
Nepieciešamā versija: Python 3.10+.

## Datu struktūra

Lietotne saglabā un nolasa izdevumus vietējā `expenses.json` failā. Dati tiek automātiski ielādēti un sakārtoti hronoloģiskā secībā katras palaišanas reizē.

Piezīme: Repozitorijā jau ir iekļauts faila paraugs ar 3 mēnešu testa datiem (vairāk nekā 800 EUR mēnesī katrā kategorijā), lai programmas analīzes un CSV eksporta funkcijas varētu izmēģināt uzreiz pēc uzstādīšanas. Sākot lietot programmu savām vajadzībām, šo failu jāizdzēš - saglabājot izdevumus, programma izveidos jaunu failu.

Katrs izdevuma ieraksts sastāv no šādiem laukiem:
*   `date` (string): Datums formātā `GGGG-MM-DD`.
*   `amount` (float): Summa eiro valūtā.
*   `category` (string): Viena no atļautajām kategorijām (Ēdiens, Transports, Izklaide, Komunālie maksājumi, Veselība, Iepirkšanās, Cits).
*   `description` (string): Īss tēriņa apraksts.

### Datu faila piemērs:
[
  {
        "date": "2026-04-18",
        "amount": 120.0,
        "category": "Iepirkšanās",
        "description": "Pavasara virsjaka"
  }
]

## Lietošana
Programma darbojas interaktīvā režīmā ar termināļa izvēlni:
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Galvenā izvēlne
──────────────────────────────────────────────────────────────────────

1) Pievienot izdevumu
2) Parādīt izdevumus
3) Filtrēt pēc mēneša
4) Kopsavilkums pa kategorijām
5) Dzēst izdevumu
6) Eksportēt CSV
7) Iziet

Izvēlies darbību (1-7):
*****************************************************



### 1. Pievienot jaunu izdevumu
Izvēloties 1. darbību, programma palūdz lietotājam pēc kārtas ievadīt nepieciešamos datus. Datuma ievadē tiek piedāvāts automātisks šodienas datums. Kategoriju atlasei tiek izmantota vienkāršota numurēta izvēlne, lai paātrinātu datu ievadi un novērstu pārrakstīšanās kļūdas.
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Pievienot jaunu izdevumu
──────────────────────────────────────────────────────────────────────


Datums (YYYY-MM-DD), atstājot tukšu, tiks paņemts šodienas datums (2026-05-17): 2026-05-17
Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Komunālie maksājumi 5) Veselība 6) Iepirkšanās 7) Cits
Izvēlies numuru (1-7): 2
Summa (EUR): 4.50
Apraksts: Vilciena biļete
*****************************************************



### 2. Parādīt izdevumus
No JSON faila tiek nolasīti visi saglabātie izdevumi. Dati terminālī tiek attēloti hronoloģiskā secībā no vecākā uz jaunāko, apakšā parādot kopsavilkumu par kopējo iztērēto summu un ierakstu skaitu.
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Izdevumu saraksts
──────────────────────────────────────────────────────────────────────

Datums             Summa    Kategorija           Apraksts
──────────────────────────────────────────────────────────────────────
2026-03-01       225.40 EUR Komunālie maksājumi  Apkure un siltais ūdens (februāris)
2026-03-02        44.10 EUR Komunālie maksājumi  Atkritumu izvešana un apsaimniekošana
2026-03-04        78.50 EUR Ēdiens               Pārtikas krājumu papildināšana (Rimi)
....
2026-05-25        25.00 EUR Cits                 Dāvanu karte draugam
2026-05-28        12.50 EUR Cits                 Spotify mēneša abonements
──────────────────────────────────────────────────────────────────────
  KOPĀ:         2523.59 EUR (42 ieraksti)
──────────────────────────────────────────────────────────────────────

──────────────────────────────────────────────────────────────────────
Nospiediet [Enter], lai atgrieztos izvēlnē...
*****************************************************



### 3. Filtrēt pēc mēneša
Šī funkcija vispirms atrod un parāda tikai tos mēnešus, kuros reāli eksistē ieraksti, sakārtojot tos dilstošā secībā (jaunākie mēneši augšgalā). Pēc numura izvēles programma izfiltrē un parāda tikai atlasītā mēneša izdevumu sarakstu un konkrētā mēneša kopsummu.
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Filtrēt pēc mēneša
──────────────────────────────────────────────────────────────────────


      Pieejamie mēneši
──────────────────────────────
1) 2026-05
2) 2026-04
3) 2026-03

Izvēlieties numuru (1-3): 1
*****************************************************

*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Izdevumu saraksts (2026-05)
──────────────────────────────────────────────────────────────────────

Datums             Summa    Kategorija           Apraksts
──────────────────────────────────────────────────────────────────────
2026-05-01       165.40 EUR Komunālie maksājumi  NĪN un apsaimniekošanas rēķins
2026-05-02        48.90 EUR Komunālie maksājumi  Internets un televīzija
...
2026-05-28        12.50 EUR Cits                 Spotify mēneša abonements
──────────────────────────────────────────────────────────────────────
  KOPĀ:          888.05 EUR (15 ieraksti)
──────────────────────────────────────────────────────────────────────

──────────────────────────────────────────────────────────────────────
Nospiediet [Enter], lai atgrieztos izvēlnē...
*****************************************************



### 4. Kopsavilkums pa kategorijām
Programma veic visu sistēmā esošo datu grupēšanu, saskaitot tēriņus katrā kategorijā. Tas lietotājam sniedz ātru un strukturētu pārskatu par to, kurām dzīves sfērām tiek tērēts visvairāk finanšu līdzekļu.
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Kopsavilkums pa kategorijām
──────────────────────────────────────────────────────────────────────

Kategorija                  Summa
────────────────────────────────────
Komunālie maksājumi       516.05 EUR
Ēdiens                    306.70 EUR
Transports                268.00 EUR
Veselība                  216.10 EUR
Izklaide                  220.00 EUR
Iepirkšanās               651.34 EUR
Cits                      120.00 EUR
────────────────────────────────────
  KOPĀ:                  2298.19 EUR

──────────────────────────────────────────────────────────────────────
Nospiediet [Enter], lai atgrieztos izvēlnē...
*****************************************************



### 5. Dzēst izdevumu
Dzēšanas režīmā visi izdevumi tiek numurēti. Lietotājam jānosaka dzēšamo ierakstu un jievadA tā numuru. Pēc apstiprināšanas ieraksts tiek izdzēsts gan no operatīvās atmiņas saraksta, gan automātiski pārrakstīts JSON failā.
*****************************************************

======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Izdevumu saraksts
──────────────────────────────────────────────────────────────────────

Nr.  Datums             Summa    Kategorija           Apraksts
──────────────────────────────────────────────────────────────────────
1)   2026-03-01       225.40 EUR Komunālie maksājumi  Apkure un siltais ūdens (februāris)
2)   2026-03-02        44.10 EUR Komunālie maksājumi  Atkritumu izvešana un apsaimniekošana
3)   2026-03-04        78.50 EUR Ēdiens               Pārtikas krājumu papildināšana (Rimi)
4)   2026-03-06        22.30 EUR Ēdiens               Svaigi dārzeņi un augļi (Tirgus)
5)   2026-03-08        65.00 EUR Transports           Degviela (Neste)
6)   2026-03-10        18.00 EUR Transports           Auto stāvvietas abonements
...
41)  2026-05-25        25.00 EUR Cits                 Dāvanu karte draugam
42)  2026-05-28        12.50 EUR Cits                 Spotify mēneša abonements
──────────────────────────────────────────────────────────────────────
  KOPĀ:         2523.59 EUR (42 ieraksti)
──────────────────────────────────────────────────────────────────────
Ievadiet ieraksta numuru, kuru vēlaties dzēst (vai 0, lai atceltu): 1
*****************************************************

*****************************************************
Izdzēsts: Apkure un siltais ūdens (februāris) (225.4 EUR)
Saraksts atjaunināts un saglabāts.

──────────────────────────────────────────────────────────────────────
Nospiediet [Enter], lai atgrieztos izvēlnē...
*****************************************************



### 6. Eksportēt CSV
Izvēloties 6. punktu, visi izdevumi no JSON faila tiek transformēti un saglabāti failā izdevumi_eksports.csv. Fails ir pilnībā optimizēts tūlītējai atvēršanai Microsoft Excel (izmantots ',' atdalītājs un UTF-8 kodējums latviešu burtiem).
*****************************************************
======================================================================
  IZDEVUMU IZSEKOTĀJS
======================================================================
    Eksportēt CSV
──────────────────────────────────────────────────────────────────────



      ✅ Dati veiksmīgi eksportēti uz failu: izdevumi_eksports.csv




──────────────────────────────────────────────────────────────────────
Nospiediet [Enter], lai atgrieztos izvēlnē...
*****************************************************


### 7. Iziet
Aptur programmas saskarni, aizver visus atvērtos resursus un droši pabeidz darbu komandrindā.
*****************************************************
Uz redzēšanos!

C:\DEV\final-project\expense_tracker>
*****************************************************

## Autors
Uldis Upāns — Programmēšanas pamati, 2026
