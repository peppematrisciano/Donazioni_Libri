from django.contrib import admin

from .models import Donatore, Autore, Acquirente, Donazione, Libro, Amministratore, Genere, LibroAcquistato

admin.site.register(Donatore)
admin.site.register(Autore)
admin.site.register(Acquirente)
admin.site.register(Amministratore)
admin.site.register(Donazione)
admin.site.register(Libro)
admin.site.register(Genere)
admin.site.register(LibroAcquistato)
