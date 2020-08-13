from django.shortcuts import render
from .models import *

def Accueil(request):
    return render(request,'index.html')

def toauthenticate(request):
    return render(request,'auth_permis.html')

def auth_permis(request):
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    date_naissance=request.POST['date_naissance']
    lieu_naissance=request.POST['lieu_naissance']
    groupe_sanguin=request.POST['groupe_sanguin'] 

    if(Permis.objects.filter(nom=nom)):
        if(Permis.objects.filter(prenom=prenom)):
            if(Permis.objects.filter(date_naissance=date_naissance)):
                if (Permis.objects.filter(lieu_naissance=lieu_naissance)):
                    if(Permis.objects.filter(groupe_sanguin=groupe_sanguin)):
                        return render(request,'auth_conducteur2.html') 
    erreur=True
    message='Vérifiez ce que vous avez saisi'
    return render(request,'auth_permis.html',locals())

def auth_permis2(request):
    numero=request.POST['numero']
    date_delivrance=request.POST['date_delivrance']
    date_expiration=request.POST['date_expiration']
    categorie_vehicule=request.POST['categorie_vehicule']

    if(Permis.objects.filter(numero=numero)):
        if(Permis.objects.filter(date_delivrance=date_delivrance)):
            if(Permis.objects.filter(date_expiration=date_expiration)):
                if (Permis.objects.filter(categorie_vehicule=categorie_vehicule)): 
                    return render(request,'register.html') 
    erreur=True
    message='Vérifiez ce que vous avez saisi'
    return render(request,'auth_permis2.html',locals())


def login(request):
    return render(request,'login.html') 

def logged(request):
    utilisateur=request.POST['utilisateur']
    username=request.POST['username']
    password=request.POST['password']
    message='Vérifiez ce que vous avez saisi'
    if utilisateur=='conducteur':
        if(Conducteur.objects.filter(username=username)):
            if(Conducteur.objects.filter(password=password)):
                return render(request,'navConducteur.html') 
        erreur=True 
        return render(request,'login.html',locals())     
    
    if utilisateur=='agent':
        if(AgentSecurite.objects.filter(username=username)):
            if(AgentSecurite.objects.filter(password=password)):
                return render(request,'navAgent.html') 
        erreur=True 
        return render(request,'login.html',locals())

    if utilisateur=='centre':
        if(CentreStage.objects.filter(username=username)):
            if(CentreStage.objects.filter(password=password)):
                return render(request,'navCentre.html') 
        erreur=True 
        return render(request,'login.html',locals()) 

def register(request):
    username=request.POST['username']
    password=request.POST['password']
    conducteur=Conducteur(username=username,password=password) 
    conducteur.save()
    return render(request,'navConducteur.html')

def profile(request):
    conducteur=Conducteur.objects.filter(permis__numero='1')
    return render(request,'profileConducteur.html',locals())

def SoldePoints(request):
    return render(request,'soldePoints.html')

def Contraventions(request):
    return render(request,'contraventions.html')

def Attestations(request):
    return render(request,'attestations.html')

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