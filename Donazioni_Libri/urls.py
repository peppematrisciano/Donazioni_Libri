"""
URL configuration for Donazioni_Libri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Donazioni import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.benvenuto, name='benvenuto'),
    path('registrazione_donatore/', views.registrazione_donatore, name='registrazione_donatore'),
    path('login_donatore/', views.login_donatore, name='login_donatore'),
    path('registrazione_acquirente/', views.registrazione_acquirente, name='registrazione_acquirente'),
    path('login_acquirente/', views.login_acquirente, name='login_acquirente'),
    path('login_amministratore/', views.login_amministratore, name='login_amministratore'),
    path('principale_donatore/', views.principale_donatore, name='principale_donatore'),
    path('principale_acquirente/', views.principale_acquirente, name='principale_acquirente'),
    path('principale_amministratore/', views.principale_amministratore, name='principale_amministratore'),
    path('logout/', views.logout, name='logout'),
    path('acquista_libro/', views.acquista_libro, name='acquista_libro'),
    path('libri_acquistati/', views.libri_acquistati, name='libri_acquistati'),
    path('rimuovi_libro/', views.rimuovi_libro, name='rimuovi_libro'),
    path('dona_libro/', views.dona_libro, name='dona_libro'),
    path('rimuovi_donazione/', views.rimuovi_donazione, name='rimuovi_donazione'),
    path('rimuovi_libro_admin/', views.rimuovi_libro_admin, name='rimuovi_libro_admin'),
    path('login_autore/', views.login_autore, name='login_autore'),
    path('principale_autore/', views.principale_autore, name='principale_autore'),
    path('create_libro/', views.create_libro, name='create_libro'),
]
