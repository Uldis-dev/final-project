# Izstrādes žurnāls

## 1. solis — sagatavošanās

Izveidoju projekta mapi uz lokālā datora:

```text
C:\DEV\final-project
```

Pieslēdzu Git versiju kontroli un izveidoju GitHub repozitoriju:

```text
https://github.com/Uldis-dev/final-project
```

Izveidoju arī sākotnējās dokumentācijas failu sagataves.

---

## 2. solis — plānošana

Izveidoju programmas plānu failā:

```text
docs/plan.md
```

Grūtākais bija saprast, cik detalizēti jāapraksta programma un tās iespējamie risinājumi.

---

## 3. solis — pirmais izstrādes etaps

Sāku veidot datu saglabāšanu un nolasīšanu JSON failā.

Izveidoju `storage.py`, par pamatu izmantojot 4. nedēļas darbu ar iepirkumu sarakstu. Pārsaucu funkcijas un pielāgoju tās izdevumu sistēmai.

Izveidoju `logic.py` ar funkciju:

```python
sum_total(expenses)
```

Tā aprēķina kopējo izdevumu summu.

Sāku veidot `app.py`, kur ievietoju galveno izvēlni, programmas ciklu un izdevumu attēlošanu. Kad fails kļuva pārāk pārblīvēts, izveidoju `ui.py`, kur pārvietoju visas funkcijas, kas saistītas ar lietotāja ievadi un izvadi.

Pirmā etapa beigās programma jau spēja:

- ievadīt izdevumus,
- saglabāt tos JSON failā,
- nolasīt un attēlot sarakstu.

---

## 4. solis — otrais izstrādes etaps

Pievienoju kopsavilkumu pa kategorijām ar funkciju:

```python
sum_by_category()
```

un izveidoju atbilstošu attēlošanu `ui.py`.

Uzlaboju lietotāja interfeisu un pārvietoju izvēlni uz `ui.py`.

Pievienoju filtrēšanu pēc mēneša:

```python
get_available_months()
filter_by_month()
```

Izveidoju arī izdevumu dzēšanas funkcionalitāti, papildinot `display_expenses()` ar iespēju attēlot numurētu sarakstu.

---

## 5. solis — trešais izstrādes etaps

Izveidoju `export.py` moduli CSV eksportam un funkciju:

```python
export_to_csv(expenses)
```

`ui.py` pievienoju eksporta statusa attēlošanu.

Noslēgumā izveidoju `README.md`. Pirmajā variantā tas GitHub izskatījās nepārskatāms, tāpēc vēlāk pārveidoju struktūru un noformējumu.