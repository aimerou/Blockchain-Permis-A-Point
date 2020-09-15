from django.shortcuts import render
from .models import *

def Accueil(request):
    return render(request,'index.html')

def toauthenticate(request):
    return render(request,'auth_permis.html')

def auth_permis1(request):
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    date_naissance=request.POST['date_naissance']
    lieu_naissance=request.POST['lieu_naissance']
    groupe_sanguin=request.POST['groupe_sanguin'] 

    if Permis.objects.filter(nom=nom, prenom=prenom, date_naissance=date_naissance, lieu_naissance=lieu_naissance, groupe_sanguin=groupe_sanguin):
        return render(request,'auth_permis2.html')
    else:
        erreur=True
        message='Vérifiez ce que vous avez saisi'
        return render(request,'auth_permis2.html',locals())

def auth_permis2(request):
    numero=request.POST['numero']
    date_delivrance=request.POST['date_delivrance']
    date_expiration=request.POST['date_expiration']
    categorie_vehicule=request.POST['categorie_vehicule']

    if Permis.objects.filter(numero=numero, date_delivrance=date_delivrance, date_expiration=date_expiration, categorie_vehicule=categorie_vehicule):
        return render(request,'register.html')
    else:
        erreur=True
        message='Vérifiez ce que vous avez saisi'
        return render(request,'register.html',locals())

def Choice_login(request):
    return render(request,'choice_login.html')

def login(request):
    utilisateur=request.POST['utilisateur']
    return render(request,'login.html',locals()) 

def logged_conducteur(request):
    username=request.POST['username']
    password=request.POST['password']
    message='Vérifiez ce que vous avez saisi'
    if Conducteur.objects.filter(username=username, password=password):
        return render(request,'navConducteur.html',locals())
    else:
        erreur=True
        return render(request,'login.html',locals())    

def logged_agent(request):
    username=request.POST['username']
    password=request.POST['password']
    message='Vérifiez ce que vous avez saisi'    
    if AgentSecurite.objects.filter(username=username, password=password):
        return render(request,'navAgent.html') 
    else:
        erreur=True 
        return render(request,'login.html',locals())

def logged_centre(request):
    name=request.POST['username']
    password=request.POST['password']
    message='Vérifiez ce que vous avez saisi'
    if CentreStage.objects.filter(nom=name, password=password):
        return render(request,'navCentre.html') 
    else:
        erreur=True 
        return render(request,'login.html',locals())

def register(request):
    username=request.POST['username']
    password=request.POST['password']
    conducteur=Conducteur(username=username,password=password) 
    conducteur.save()
    return render(request,'navConducteur.html',locals())

def SoldePoints(request):
    return render(request,'soldePoints.html')

def Contraventions(request,username):
    username=username
    contraventions=Contravention.objects.filter(destinataire__username=username)
    contra_1 = contraventions.filter(categorie=1)
    contra_2 = contraventions.filter(categorie=2)
    contra_3 = contraventions.filter(categorie=3)
    contra_4 = contraventions.filter(categorie=4)
    contra_5 = contraventions.filter(categorie=5)
    return render(request,'contraventions.html',locals())

def Attestations(request,username):
    username=username
    attestations=Attestation.objects.filter(stagiaire__username=username)
    attest_1=attestations.filter(categorie="A")
    attest_2 = attestations.filter(categorie='B')
    attest_3 = attestations.filter(categorie='C')
    attest_4 = attestations.filter(categorie='D')
    attest_5 = attestations.filter(categorie='E')
    return render(request,'attestations.html',locals())

def EnvoiContravention(request):
    return render(request,'navAgent.html')

def EnvoiAttestation(request):
    return render(request,'navCentre.html')
    
def TransactionView(request,num_permis,points):
    transaction = Transaction()
    permis = Permis.objects.get(numero=num_permis)
    transaction.conducteur = Conducteur.objects.get(conducteur=permis)
    transaction.points = points
    transaction.save()
    return render(request,'navConducteur.html')