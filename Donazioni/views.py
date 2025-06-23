from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Donatore, Acquirente, Amministratore, Autore, Libro, Donazione, LibroAcquistato, Genere

# Create your views here.
def benvenuto(request):
    return render(request, 'benvenuto.html')

def registrazione_donatore(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if username already exists
        if Donatore.objects.filter(username=username).exists():
            return render(request, 'registrazione_donatore.html', {'error': 'Username già esistente'})

        # Create new donor
        donatore = Donatore(nome=nome, cognome=cognome, username=username, password=password, email=email)
        donatore.save()

        return redirect('login_donatore')

    return render(request, 'registrazione_donatore.html')

def login_donatore(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            donatore = Donatore.objects.get(username=username, password=password)
            request.session['donatore_username'] = donatore.username
            return redirect('principale_donatore')
        except Donatore.DoesNotExist:
            return render(request, 'login_donatore.html', {'error': 'Credenziali non valide'})

    return render(request, 'login_donatore.html')

def registrazione_acquirente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if username already exists
        if Acquirente.objects.filter(username=username).exists():
            return render(request, 'registrazione_acquirente.html', {'error': 'Username già esistente'})

        # Create new buyer
        acquirente = Acquirente(nome=nome, cognome=cognome, username=username, password=password, email=email)
        acquirente.save()

        return redirect('login_acquirente')

    return render(request, 'registrazione_acquirente.html')

def login_acquirente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            acquirente = Acquirente.objects.get(username=username, password=password)
            request.session['acquirente_username'] = acquirente.username
            return redirect('principale_acquirente')
        except Acquirente.DoesNotExist:
            return render(request, 'login_acquirente.html', {'error': 'Credenziali non valide'})

    return render(request, 'login_acquirente.html')

def login_amministratore(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            amministratore = Amministratore.objects.get(username=username, password=password)
            # Note: In a real application, you would use proper password hashing
            request.session['amministratore_username'] = amministratore.username
            return redirect('principale_amministratore')
        except Amministratore.DoesNotExist:
            return render(request, 'login_amministratore.html', {'error': 'Credenziali non valide'})

    return render(request, 'login_amministratore.html')

def principale_donatore(request):
    if 'donatore_username' not in request.session:
        return redirect('login_donatore')

    donatore = Donatore.objects.get(username=request.session['donatore_username'])
    donazioni = Donazione.objects.filter(donatore=donatore)
    libri = Libro.objects.all()

    return render(request, 'principale_donatore.html', {'donatore': donatore, 'donazioni': donazioni, 'libri': libri})

def principale_acquirente(request):
    if 'acquirente_username' not in request.session:
        return redirect('login_acquirente')

    acquirente = Acquirente.objects.get(username=request.session['acquirente_username'])
    libri_disponibili = Libro.objects.filter(quantita_disponibili__gt=0)

    return render(request, 'principale_acquirente.html', {'acquirente': acquirente, 'libri': libri_disponibili})

def principale_amministratore(request):
    if 'amministratore_username' not in request.session:
        return redirect('login_amministratore')

    amministratore = Amministratore.objects.get(username=request.session['amministratore_username'])
    donazioni = Donazione.objects.all()
    libri = Libro.objects.all()

    return render(request, 'principale_amministratore.html', {'amministratore': amministratore, 'donazioni': donazioni, 'libri': libri})

def logout(request):
    if 'donatore_username' in request.session:
        del request.session['donatore_username']
    if 'acquirente_username' in request.session:
        del request.session['acquirente_username']
    if 'amministratore_username' in request.session:
        del request.session['amministratore_username']
    if 'autore_username' in request.session:
        del request.session['autore_username']

    return redirect('benvenuto')

def acquista_libro(request):
    if 'acquirente_username' not in request.session:
        return redirect('login_acquirente')

    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')
        acquirente = Acquirente.objects.get(username=request.session['acquirente_username'])

        try:
            libro = Libro.objects.get(ISBN=libro_id)

            # Check if the book is already purchased by this acquirente
            if LibroAcquistato.objects.filter(acquirente=acquirente, libro=libro).exists():
                return redirect('principale_acquirente')

            # Decrement the available quantity
            current_quantity = int(libro.quantita_disponibili)
            if current_quantity > 0:
                libro.quantita_disponibili = str(current_quantity - 1)
                libro.save()

                # Create a new purchase record
                acquisto = LibroAcquistato(
                    acquirente=acquirente,
                    libro=libro,
                    data_acquisto=timezone.now()
                )
                acquisto.save()
                return redirect('libri_acquistati')
            else:
                return redirect('principale_acquirente')
        except Libro.DoesNotExist:
            return redirect('principale_acquirente')

    return redirect('principale_acquirente')

def libri_acquistati(request):
    if 'acquirente_username' not in request.session:
        return redirect('login_acquirente')

    acquirente = Acquirente.objects.get(username=request.session['acquirente_username'])
    acquisti = LibroAcquistato.objects.filter(acquirente=acquirente)

    return render(request, 'libri_acquistati.html', {'acquirente': acquirente, 'acquisti': acquisti})

def rimuovi_libro(request):
    if 'acquirente_username' not in request.session:
        return redirect('login_acquirente')

    if request.method == 'POST':
        acquisto_id = request.POST.get('acquisto_id')
        acquirente = Acquirente.objects.get(username=request.session['acquirente_username'])

        try:
            acquisto = LibroAcquistato.objects.get(ID=acquisto_id, acquirente=acquirente)
            libro = acquisto.libro

            # Increment the available quantity
            current_quantity = int(libro.quantita_disponibili)
            libro.quantita_disponibili = str(current_quantity + 1)
            libro.save()

            # Delete the purchase record
            acquisto.delete()

            return redirect('libri_acquistati')
        except LibroAcquistato.DoesNotExist:
            return redirect('libri_acquistati')

    return redirect('libri_acquistati')

def dona_libro(request):
    if 'donatore_username' not in request.session:
        return redirect('login_donatore')

    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')
        donatore = Donatore.objects.get(username=request.session['donatore_username'])

        try:
            libro = Libro.objects.get(ISBN=libro_id)

            # Increment the available quantity
            current_quantity = int(libro.quantita_disponibili)
            libro.quantita_disponibili = str(current_quantity + 1)
            libro.save()

            # Create a new donation record
            donazione = Donazione(
                donatore=donatore,
                libro=libro,
                data=timezone.now().strftime('%Y-%m-%d')
            )
            donazione.save()

            return redirect('principale_donatore')
        except Libro.DoesNotExist:
            return redirect('principale_donatore')

    return redirect('principale_donatore')

def rimuovi_donazione(request):
    if 'donatore_username' not in request.session:
        return redirect('login_donatore')

    if request.method == 'POST':
        donazione_id = request.POST.get('donazione_id')
        donatore = Donatore.objects.get(username=request.session['donatore_username'])

        try:
            donazione = Donazione.objects.get(ID=donazione_id, donatore=donatore)
            libro = donazione.libro

            # Decrement the available quantity
            current_quantity = int(libro.quantita_disponibili)
            if current_quantity > 0:  # Ensure we don't go below 0
                libro.quantita_disponibili = str(current_quantity - 1)
                libro.save()

            # Delete the donation record
            donazione.delete()

            return redirect('principale_donatore')
        except Donazione.DoesNotExist:
            return redirect('principale_donatore')

    return redirect('principale_donatore')

def rimuovi_libro_admin(request):
    if 'amministratore_username' not in request.session:
        return redirect('login_amministratore')

    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')

        try:
            libro = Libro.objects.get(ISBN=libro_id)

            # Delete the book record
            libro.delete()

            return redirect('principale_amministratore')
        except Libro.DoesNotExist:
            return redirect('principale_amministratore')

    return redirect('principale_amministratore')

def login_autore(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            autore = Autore.objects.get(username=username, password=password)
            request.session['autore_username'] = autore.username
            return redirect('principale_autore')
        except Autore.DoesNotExist:
            return render(request, 'login_autore.html', {'error': 'Credenziali non valide'})

    return render(request, 'login_autore.html')

def principale_autore(request):
    if 'autore_username' not in request.session:
        return redirect('login_autore')

    autore = Autore.objects.get(username=request.session['autore_username'])
    libri = Libro.objects.filter(autore=autore)
    generi = Genere.objects.all()

    return render(request, 'principale_autore.html', {'autore': autore, 'libri': libri, 'generi': generi})

def create_libro(request):
    if 'autore_username' not in request.session:
        return redirect('login_autore')

    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        titolo = request.POST.get('titolo')
        editore = request.POST.get('editore')
        anno_pubblicazione = request.POST.get('anno_pubblicazione')
        edizione = request.POST.get('edizione')
        lingua = request.POST.get('lingua')
        copertina_rigida = request.POST.get('copertina_rigida')
        materia = request.POST.get('materia')
        classe_scolastica = request.POST.get('classe_scolastica')
        data_pubblicazione = request.POST.get('data_pubblicazione')
        genere_nome = request.POST.get('genere')
        quantita_disponibili = request.POST.get('quantita_disponibili')

        # Check if ISBN already exists
        if Libro.objects.filter(ISBN=isbn).exists():
            autore = Autore.objects.get(username=request.session['autore_username'])
            libri = Libro.objects.filter(autore=autore)
            generi = Genere.objects.all()
            return render(request, 'principale_autore.html', {
                'autore': autore, 
                'libri': libri, 
                'generi': generi, 
                'error': 'ISBN già esistente'
            })

        try:
            autore = Autore.objects.get(username=request.session['autore_username'])
            genere = Genere.objects.get(nome_genere=genere_nome)

            # Create new book
            libro = Libro(
                ISBN=isbn,
                titolo=titolo,
                editore=editore,
                anno_pubblicazione=anno_pubblicazione,
                edizione=edizione,
                lingua=lingua,
                copertina_rigida=copertina_rigida,
                materia=materia,
                classe_scolastica=classe_scolastica,
                data_pubblicazione=data_pubblicazione,
                autore=autore,
                genere=genere,
                quantita_disponibili=quantita_disponibili
            )
            libro.save()

            libri = Libro.objects.filter(autore=autore)
            generi = Genere.objects.all()
            return render(request, 'principale_autore.html', {
                'autore': autore, 
                'libri': libri, 
                'generi': generi, 
                'success': 'Libro creato con successo'
            })
        except Exception as e:
            autore = Autore.objects.get(username=request.session['autore_username'])
            libri = Libro.objects.filter(autore=autore)
            generi = Genere.objects.all()
            return render(request, 'principale_autore.html', {
                'autore': autore, 
                'libri': libri, 
                'generi': generi, 
                'error': f'Errore durante la creazione del libro: {str(e)}'
            })

    return redirect('principale_autore')
