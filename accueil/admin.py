from django.contrib import admin
from accueil.models import Product

# Register your models here.
@admin.register(Product)  # Le nom de la classe de modèle doit être utilisé ici
class ProductAdmin(admin.ModelAdmin):  # Il est conventionnel d'utiliser le nom du modèle suivi de 'Admin'
    list_display = ('name', 'price', 'description', 'image')  
