from faker import Faker  # Importiamo la libreria Faker per generare dati casuali
import openpyxl  # Importiamo la libreria openpyxl per creare file Excel

# Creiamo un'istanza di Faker per generare dati casuali
fake = Faker()

# Creiamo una lista per contenere i dati degli utenti
utenti = []

# Generiamo i dati per 10 utenti
for _ in range(10):
    # Ogni utente ha attributi nome, cognome, email e telefono
    utente = {
        "Nome": fake.first_name(),
        "Cognome": fake.last_name(),
        "Email": fake.email(),
        "Telefono": fake.phone_number()
    }
    utenti.append(utente)  # Aggiungiamo l'utente alla lista

# Creiamo un nuovo file Excel
wb = openpyxl.Workbook()  # Inizializziamo una cartella di lavoro Excel
sheet = wb.active  # Selezioniamo il foglio attivo

# Aggiungiamo i titoli delle colonne
sheet.append(["Nome", "Cognome", "Email", "Telefono"])

# Inseriamo i dati degli utenti nel foglio Excel
for utente in utenti:
    sheet.append([utente["Nome"], utente["Cognome"], utente["Email"], utente["Telefono"]])

# Salviamo il file Excel
wb.save("utenti.xlsx")  # Il file sarà salvato con questo nome

print("File Excel 'utenti.xlsx' creato con successo!")
