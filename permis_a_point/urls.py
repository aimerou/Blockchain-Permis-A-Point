from django.urls import path
from . import views

urlpatterns = [
     path('accueil', views.Accueil, name='accueil'),
     path('soldePoints', views.SoldePoints, name='soldePoints'),
     path('conducteur/contraventions/<str:username>', views.Contraventions, name='contraventions'),
     path('conducteur/attestations/<str:username>', views.Attestations, name='attestations'),
     path('agent/contraventionEnvoyee', views.EnvoiContravention, name='envoi_contravention'),
     path('centre/attestationEnvoyee', views.EnvoiAttestation, name='envoi_attestation'),
     path('permis/authentification1',views.toauthenticate,name='to_authenticate'),
     path('permis/authentification2',views.auth_permis1,name='authentification1'),
     path('register',views.auth_permis2,name='authentification2'),
     path('conducteur/dashboard',views.register,name='new_conducteur'),
     path('choice_login',views.Choice_login,name='choice_login'),
     path('login',views.login,name='login'),
     path('conducteur/dashboard2',views.logged_conducteur,name='logged_conducteur'),
     path('agent/dashboard',views.logged_agent,name='logged_agent'),
     path('centre_de_stage/dashboard',views.logged_centre,name='logged_centre'),
]