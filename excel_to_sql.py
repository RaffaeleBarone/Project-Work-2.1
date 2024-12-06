import sqlite3  # Libreria per lavorare con database SQLite
import openpyxl  # Libreria per leggere file Excel

# Leggiamo il file Excel
nome_file_excel = "utenti.xlsx"  # Nome del file Excel
workbook = openpyxl.load_workbook(nome_file_excel)  # Carichiamo il file Excel
sheet = workbook.active  # Selezioniamo il foglio attivo

# Creiamo il database SQLite (se non esiste, verrà creato)
conn = sqlite3.connect("utenti.db")  # Nome del file del database SQLite
cursor = conn.cursor()  # Creiamo un cursore per eseguire i comandi SQL

# Creiamo la tabella SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID unico per ogni utente
    nome TEXT,  -- Nome dell'utente
    cognome TEXT,  -- Cognome dell'utente
    email TEXT,  -- Email dell'utente
    telefono TEXT  -- Numero di telefono dell'utente
)
""")
print("Tabella 'utenti' creata (se non esiste già).")

# Leggiamo i dati dal file Excel e li inseriamo nella tabella SQL
for row in sheet.iter_rows(min_row=2, values_only=True):  # Partiamo dalla seconda riga
    nome, cognome, email, telefono = row  # Prendiamo i valori dalle colonne
    cursor.execute("INSERT INTO utenti (nome, cognome, email, telefono) VALUES (?, ?, ?, ?)",
                   (nome, cognome, email, telefono))

print("Dati inseriti nel database SQLite.")

# Salviamo i cambiamenti e chiudiamo la connessione
conn.commit()
conn.close()
print("Database salvato e connessione chiusa.")
