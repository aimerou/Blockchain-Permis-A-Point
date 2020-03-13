from django.urls import path
from . import views

urlpatterns = [
     path('accueil', views.Accueil, name='accueil'),
     path('inscription', views.Inscription, name='inscription'), 

     path('authentification1',views.toauthenticate,name='authentification1'),
     path('authentification2',views.auth_conducteur,name='authentification2'),
     path('register',views.auth_conducteur2,name='register'),
     path('conducteur',views.register,name='navConducteur'),
     path('login',views.login,name='login'),

     path('bienvenue',views.logged,name='logged'), 

     path('index',views.index),
      
     path('profile',views.profile,name='profile'),
      
]