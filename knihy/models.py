from django.db import models

# Create your models here.

class Zanr(models.Model):
    nazev_zanru = models.CharField(max_length=80, verbose_name="Žánr")

    def __str__(self):
        return "Nazev_zanru: {0}".format(self.nazev_zanru)

    class Meta:
        verbose_name = "Žánr"
        verbose_name_plural = "Žánry"

class Kniha(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název knihy")
    autor = models.CharField(max_length=180, verbose_name="Autor")
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True, verbose_name="Žánr")

    def __str__(self):
        return "Nazev: {0} | Autor: {1} | Zanr: {2}".format(self.nazev, self.autor, self.zanr.nazev_zanru)

    class Meta:
        verbose_name = "Kniha"
        verbose_name_plural = "Knihy"