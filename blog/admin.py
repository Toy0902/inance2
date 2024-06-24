from django.contrib import admin
from blog.models import Profil,Email

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ['nom', 'rasmi']

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']