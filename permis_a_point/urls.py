from django.urls import path
from . import views

urlpatterns = [
     path('accueil', views.Accueil, name='accueil'),
     path('inscription', views.Inscription, name='inscription'),
     path('connexion', views.Connexion, name='connexion'),
     path('dashboardConducteur', views.DashboardConducteur, name='dashboardConducteur'),
     path('dashboardAgentSecurite', views.DashboardAgentSecurite, name='dashboardAgentSecurite'),
     path('dashboardCentreStage', views.DashboardCentreStage, name='dashboardCentreStage'),
]