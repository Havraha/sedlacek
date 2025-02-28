from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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


class UzivatelManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user

    # Vytvoří admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user


class Uzivatel(AbstractBaseUser):
    email = models.EmailField(max_length=300, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True