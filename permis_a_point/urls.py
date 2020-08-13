from django.urls import path
from . import views

urlpatterns = [
     path('accueil', views.Accueil, name='accueil'),
     path('soldePoints', views.SoldePoints, name='soldePoints'),
     path('conducteur/contraventions', views.Contraventions, name='contraventions'),
     path('conducteur/attestations', views.Attestations, name='attestations'),
     path('agent/contraventionEnvoyee', views.EnvoiContravention, name='envoi_contravention'),
     path('centre/attestationEnvoyee', views.EnvoiAttestation, name='envoi_attestation'),
     path('permis/authentification1',views.toauthenticate,name='authentification1'),
     path('permis/authentification2',views.auth_permis,name='authentification2'),
     path('register',views.auth_permis2,name='register'),
     path('login',views.login,name='login'),
     path('bienvenue',views.logged,name='logged'),
     path('conducteur/profile',views.profile,name='profile'),
]