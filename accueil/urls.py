# Dans l'application accueil, dans le fichier urls.py
from django.urls import path
from .views import index  # Importez vos vues correctement ici
from. import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_view
from .forms import LoginForm

app_name = 'accueil'  # C'est une bonne pratique de définir un espace de nom pour les URL de l'application

urlpatterns = [
    path('', index, name='home'),  # Ceci est pour la racine de 'accueil'
    path('page1/', index, name='page1'),  # Vous pouvez ajouter d'autres chemins ici
    path('adresse/', views.address, name='address'),
    path('category/<str:val>', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', views.productDetail.as_view(), name='product-detail'),
    path ('connexion/', views.connexion, name='connexion'),
    path('category-name/<str:val>', views.CategoryName.as_view(), name='category-name'),

    #login authentification

    path('inscription/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='accueil/connexion.html',  authentication_form=LoginForm,  ), name='login'),
]