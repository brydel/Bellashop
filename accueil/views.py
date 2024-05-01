from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from .models import Product
from django.db.models import Count
from . forms import CustumerRegistrationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

# Create your views here.
def index(request):
    popular_products = Product.objects.filter(Category='Populaire')[:3]  # Limite à trois produits
    return render(request, 'accueil/index.html', {'popular_products': popular_products})

def address(request):
    return render(request, 'accueil/addresse.html')

def cart(request):
    return render(request, 'accueil/carte.html')
def connexion(request):
    return render(request, 'accueil/connexion.html')
def newpassword(request):
    return render(request, 'accueil/newpassword.html') 
def paiement(request):
    return render(request, 'accueil/paiment.html')
def product(request):
    return render(request, 'accueil/produit.html')
def resetpassword(request):
    return render(request, 'accueil/resetpassword.html')
def incription(request):
    return render(request, 'accueil/incription.html')
def details(request):
    return render(request, 'accueil/details.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(Category=val)
        name = Product.objects.filter(Category=val).values('name').annotate(total = Count('name'))
        context = {
        
    }
        return render(request, 'accueil/category.html',locals())
    
class productDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        savings = product.price - product.discounted_price
        context = {
        'product': product,
        'savings': savings,
        }
        return render(request, 'accueil/productdetail.html',locals())
    
class CategoryName(View):
    def get(self, request, val):
        product = Product.objects.filter(name=val)
        name = Product.objects.filter(Category =product[0].Category).values('name')
        context = {

    }
        return render(request, 'accueil/category.html',locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustumerRegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'accueil/incription.html', locals())

    def post(self, request):
        form = CustumerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès!')
        else:
            messages.warning(request, 'Veuillez remplir le formulaire correctement')
        context = {
            'form': form
        }
        return render(request, 'accueil/incription.html', locals())
    

