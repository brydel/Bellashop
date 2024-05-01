from django.db import models

# Create your models here.

CATEGORY_CHOISES =(
    ('GC', 'Games De Chere' ),
    ('PI', 'Produit vendu individuellement'),
    ('autres', 'Autres'),
    ('Populaire', 'populaire'),
)
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Command(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    Category = models.CharField(max_length=50, choices=CATEGORY_CHOISES, default='Populaire')
    date_modified = models.DateTimeField(auto_now=True)
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    popular_products = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    