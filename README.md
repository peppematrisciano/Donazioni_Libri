# BookCycle – Piattaforma per il riciclo solidale dei libri

Giuseppe Matrisciano 0334000140

Progetto sviluppato in Python Django per la gestione del riciclo di libri scolastici e non.
Permette la donazione, la pubblicazione e l’acquisto di libri da parte di utenti registrati (donatori, acquirenti, amministratori, autori).
Il ricavato finanzia biblioteche, associazioni culturali e progetti educativi.

## Funzionalità principali

- Registrazione e login di utenti (donatori, acquirenti, amministratori, autori)
- Donazione di libri da parte dei donatori
- Pubblicazione e gestione dei libri da parte degli amministratori
- Acquisto di libri da parte degli acquirenti
- Gestione degli autori e dei generi dei libri
- Visualizzazione della disponibilità dei libri


## Installazione
Per scaricare la repository eseguire il comando:
```
git clone https://github.com/peppematrisciano/Donazioni_libri.git
```
Una volta fatto ciò, entrare nella cartella `Donazioni` ed eseguire da terminale:
```
# Da powershell o cmd
python -m venv venv
```
E poi:
```
# Da PowerShell
venv/Scripts/activate
# Oppure
venv/Scripts/activate.ps1

# Da cmd
venv/Scripts/activate.bat
```
Ora che l'ambiente virtuale è attivo, è possibile installare le dipendenze con:
```
python -m pip install -r requirements.txt
```

## Utilizzo

Per avviare il server eseguire:
```
py manage.py runserver
```

Utenti di prova già registrati:

Donatore:
```
username: jeff_bezos
passw: amazon
```
Autore:
```
username: J.K. Rowling
passw: rowling
```
Acquirente:
```
username: mario_rossi
passw:mario
```
Amministratore:
```
username: luigi_amendola
passw:luigi
```
