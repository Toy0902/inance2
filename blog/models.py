from django.db import models


class Profil(models.Model):
    nom = models.CharField(max_length=120)
    rasmi = models.ImageField(upload_to='rasm/images')

    def __str__(self):
        return self.nom

class Email(models.Model):
    email = models.CharField(max_length=222)
    text = models.TextField()
    numbers = models.IntegerField()
    ismi = models.CharField(max_length=300)

    def __str__(self):
        return self.ismi
