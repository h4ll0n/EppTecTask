# SQL ukol pro eppTec - Datovy model + queries


import sqlite3

# Novy data soubor
db_file = 'eppBank.db'

# Připojení k databázi
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Vytvoření tabulek
cursor.execute('''
    CREATE TABLE Klient (
        id_klient INTEGER PRIMARY KEY,
        jmeno TEXT,
        prijmeni TEXT,
        email TEXT,
        telefon TEXT,
        adresa TEXT
    )
''')

# Vytvoření tabulky Ucet
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ucet (
        id_ucet INTEGER PRIMARY KEY,
        id_klient INTEGER,
        FOREIGN KEY (id_klient) REFERENCES Klient(id_klient)
    )
''')

# Vytvoření tabulky Transakce
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transakce (
        id_transakce INTEGER PRIMARY KEY,
        id_ucet INTEGER,
        datum DATE,
        castka REAL,
        typ_transakce INTEGER,
        FOREIGN KEY (id_ucet) REFERENCES Ucet(id_ucet)
        FOREIGN KEY (typ_transakce) REFERENCES TypTransakce(id_typ_transakce)
    )
''')

# Vytvoření tabulky Balance
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Balance (
        id_balance INTEGER PRIMARY KEY,
        id_ucet INTEGER,
        datum DATE,
        jistina REAL,
        FOREIGN KEY (id_ucet) REFERENCES Ucet(id_ucet)
    )
''')

# Vytvoření tabulky TypTransakce pro číselník typů transakcí
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TypTransakce (
        id_typ_transakce INTEGER PRIMARY KEY,
        nazev TEXT
    )
''')

# Uložení změn a uzavření spojení
conn.commit()
conn.close()

# Připojení k databázi
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit,
# že suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.

cursor.execute('''
SELECT Klient.id_klient, Klient.jmeno, Klient.prijmeni, SUM(Balance.jistina) as total_jistina
FROM Klient
JOIN Ucet ON Klient.id_klient = Ucet.id_klient
JOIN Balance ON Ucet.id_ucet = Balance.id_ucet
WHERE strftime('%Y-%m', Balance.datum) = strftime('%Y-%m', 'now', 'start of month', '-1 month')
GROUP BY Klient.id_klient
HAVING total_jistina > :cislo_c;
''')

conn.close()

#10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta) k ultimu měsíce a tuto na konci řádku vždy zobrazte.

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''
SELECT Klient.id_klient, Klient.jmeno, Klient.prijmeni, SUM(Balance.jistina) as total_pohledavka
FROM Klient
JOIN Ucet ON Klient.id_klient = Ucet.id_klient
JOIN Balance ON Ucet.id_ucet = Balance.id_ucet
WHERE strftime('%Y-%m', Balance.datum) = strftime('%Y-%m', 'now', 'start of month')
GROUP BY Klient.id_klient
ORDER BY total_pohledavka DESC
LIMIT 10;
''')

# Zobrazení výsledků
results = cursor.fetchall()
for row in results:
    print(row)

# Uzavření spojení
conn.close()
