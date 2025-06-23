from django.db import models

class Donatore(models.Model):

    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f"{self.username} - {self.nome} {self.cognome}"



class Autore(models.Model):

    username = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.username} - {self.nome} {self.cognome}"


class Acquirente(models.Model):


    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f"{self.username} - {self.nome} {self.cognome}"



class Amministratore(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f"{self.username} - {self.nome} {self.cognome}"



class Genere(models.Model):
    nome_genere = models.CharField(max_length=100, primary_key=True)
    descrizione = models.TextField(null=True)

    def __str__(self):
        return self.nome_genere


class Libro(models.Model):
        ISBN = models.CharField(max_length=100, primary_key=True)
        titolo = models.CharField(max_length=100, null=True)
        editore = models.CharField(max_length=100, null=True)
        anno_pubblicazione = models.CharField(max_length=100, null=True)
        edizione = models.CharField(max_length=100, null=True)
        lingua = models.CharField(max_length=100, null=True)
        copertina_rigida = models.CharField(max_length=100, null=True)
        materia = models.CharField(max_length=100, null=True, blank=True)
        classe_scolastica = models.CharField(max_length=100, null=True, blank=True)
        data_pubblicazione = models.DateField(null=True)
        autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
        quantita_disponibili = models.CharField(max_length=100, null=True, default=0)
        genere = models.ForeignKey(Genere, on_delete=models.SET_NULL, null=True)

        def __str__(self):
            return f"{self.ISBN} - {self.titolo}"


class Donazione(models.Model):
    ID= models.AutoField(primary_key=True)
    data = models.CharField(max_length=100, null=True)
    donatore = models.ForeignKey(Donatore, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Donazione {self.ID} - {self.donatore.username} - {self.libro.titolo if self.libro else 'Nessun libro'}"


class LibroAcquistato(models.Model):
    ID = models.AutoField(primary_key=True)
    data_acquisto = models.DateField(auto_now_add=True)
    acquirente = models.ForeignKey(Acquirente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Acquisto {self.ID} - {self.acquirente.username} - {self.libro.titolo}"
