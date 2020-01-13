"""
from django.http import HttpResponse

def index(request):
    return HttpResponse('test0222')
"""

from django.shortcuts import render

def index(request):
    return render(request, "knihy/index.html", dict(nazev_filmu="Strážci Galaxie", zanr="Fantasy", hodnoceni="11/10"))
