from django.contrib import admin
from .models import Kniha, Zanr #Importujeme si modely

#Modely registrujeme
admin.site.register(Kniha)
admin.site.register(Zanr)