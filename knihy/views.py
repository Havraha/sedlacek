"""
from django.http import HttpResponse

def index(request):
    return HttpResponse('test0222')
"""

from django.shortcuts import render, redirect
from django.views import generic
from .models import Kniha
from .forms import KnihaForm


class KnihaIndex(generic.ListView):

    template_name = "knihy/knihy_index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "kniha" # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list knih seřazených od největšího id (9,8,7...)
    def get_queryset(self):
        return Kniha.objects.all().order_by("-id")

class CurrentKnihaView(generic.DetailView):

    model = Kniha
    template_name = "knihy/kniha_detail.html"

class OblibeneKnihy(generic.ListView):
    template_name = "knihy/oblibene_knihy.html"
    context_object_name = "kniha"

    def get_queryset(self):
        return Kniha.objects.all().order_by("-id")

class CreateKniha(generic.edit.CreateView):

    form_class = KnihaForm
    template_name = "knihy/create_kniha.html"

# Metoda pro GET request, zobrazí pouze formulář
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

# Metoda pro POST request, zkontroluje formulář; pokud je validní, vytvoří novou knihu; pokud ne, zobrazí formulář s chybovou hláškou
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
        return render(request, self.template_name, {"form":form})