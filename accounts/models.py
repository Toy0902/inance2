from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to="users/", blank=True, null=True)
    data_of_birth = models.DateField(blank=True, null=True)

    def str(self):
        return f"{self.user} ning profili"

# Create your models here.
from django.db import models

# Create your models here.
