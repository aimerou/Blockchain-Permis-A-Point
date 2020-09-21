from django.urls import path
from . import views

urlpatterns = [
     path('accueil', views.Accueil, name='accueil'),
     path('blockchain/<str:nom>', views.Blockchain, name='blockchain'),
     path('block/<int:index>', views.Bloc, name='block'),
     path('soldePoints', views.SoldePoints, name='soldePoints'),
     path('conducteur/contraventions/<str:username>', views.Contraventions, name='contraventions'),
     path('conducteur/attestations/<str:username>', views.Attestations, name='attestations'),
     path('permis/authentification1',views.toauthenticate,name='to_authenticate'),
     path('register',views.auth_permis,name='authentification'),
     path('conducteur/dashboard/<int:numero>',views.register,name='new_conducteur'),
     path('choice_login',views.Choice_login,name='choice_login'),
     path('login',views.login,name='login'),
     path('conducteur/dashboard2',views.logged_conducteur,name='logged_conducteur'),
     path('conducteur/dashboard/<str:username>',views.Redirect_conducteur,name='redirected_conducteur'),
     path('agent/dashboard',views.logged_agent,name='logged_agent'),
     path('contraventionEnvoyee/<str:username>', views.EnvoiContravention, name='envoi_contravention'),
     path('agent/dashboard/<str:username>',views.Redirect_agent,name='redirected_agent'),
     path('centre_de_stage/dashboard',views.logged_centre,name='logged_centre'),
     path('attestationEnvoyee/<str:name>', views.EnvoiAttestation, name='envoi_attestation'),
     path('centre_de_stage/dashboard/<str:name>',views.Redirect_centre,name='redirected_centre'),
]