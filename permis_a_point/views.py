from django.shortcuts import render
from .models import *
from datetime import datetime,timezone

def Accueil(request):
    return render(request,'index.html')

def Blockchain(request,nom):
    if Conducteur.objects.filter(username=nom):
        username = nom
        utilisateur = "conducteur"
    elif AgentSecurite.objects.filter(username=nom):
        username = nom
        utilisateur = "agent"
    elif CentreStage.objects.filter(name=nom):
        name = nom
        utilisateur = "centre"
    #Determination de la date du dernier bloc
    blocs = Block.objects.all()
    last = Block.objects.last()
    last_time = (datetime.now(timezone.utc) - last.date).total_seconds()
    minutes = int(last_time / 60)
    #On conclut si un nouveau bloc a ete cree durant la derniere minute ou pas
    if last_time > 60:
        new_block = 0
    else:
        new_block = 1
    nbre_trans = []
    for i in range(7):
        trans = 0
        for t in Transaction.objects.all():
            if t.date.weekday() == i:
                trans += 1
        nbre_trans.append(trans)
    return render(request,'blockchain.html',locals())

def Bloc(request,index):
    bloc = Block.objects.get(index=index)
    return render(request,'block.html',locals())

def toauthenticate(request):
    return render(request,'auth_permis.html')

def auth_permis(request):
    numero=request.POST['numero']
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    date_naissance=request.POST['date_naissance']
    lieu_naissance=request.POST['lieu_naissance']
    groupe_sanguin=request.POST['groupe_sanguin'] 
    if(Permis.objects.filter(numero=numero,nom=nom,prenom=prenom,date_naissance=date_naissance,lieu_naissance=lieu_naissance,groupe_sanguin=groupe_sanguin)):
        return render(request,'register.html',locals()) 
    erreur=True
    message='Vérifiez ce que vous avez saisi'
    return render(request,'auth_permis.html',locals())

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
        return render(request,'navAgent.html',locals()) 
    else:
        erreur=True 
        return render(request,'login.html',locals())

def logged_centre(request):
    name=request.POST['username']
    password=request.POST['password']
    message='Vérifiez ce que vous avez saisi'
    if CentreStage.objects.filter(nom=name, password=password):
        return render(request,'navCentre.html',locals()) 
    else:
        erreur=True 
        return render(request,'login.html',locals())

def register(request,numero):
    username=request.POST['username']
    password=request.POST['password']
    conducteur=Permis.objects.get(numero=numero)
    points=6
    driver=Conducteur(conducteur=conducteur,username=username,password=password) 
    driver.save()
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
    
def TransactionView(request,num_permis,points):
    transaction = Transaction()
    permis = Permis.objects.get(numero=num_permis)
    transaction.conducteur = Conducteur.objects.get(conducteur=permis)
    transaction.points = points
    transaction.save()
    return render(request,'navConducteur.html',locals())

def EnvoiContravention(request,username):
    agent = AgentSecurite.objects.get(username=username)
    nom_destinataire = request.POST['destinataire']
    destinataire = Conducteur.objects.get(username=nom_destinataire)
    categorie = request.POST['categorie']
    contenu = request.POST['contenu']
    contravention = Contravention(agent=agent,destinataire=destinataire,categorie=categorie,contenu=contenu)
    contravention.save()
    transaction = Transaction(conducteur=destinataire,points=categorie)
    transaction.save()
    return render(request,'contravention_envoyee.html',locals())

def EnvoiAttestation(request,name):
    centre = CentreStage.objects.get(nom=name)
    nom_stagiaire = request.POST['stagiaire']
    stagiaire = Conducteur.objects.get(username=nom_stagiaire)
    contenu = request.POST['contenu']
    attestation = Attestation(centre=centre,stagiaire=stagiaire,contenu=contenu)
    attestation.save()
    transaction = Transaction(conducteur=stagiaire,points=6)
    transaction.save()
    return render(request,'attestation_envoyee.html',locals())

def Redirect_conducteur(request,username):
    return render(request,'navConducteur.html',locals())

def Redirect_agent(request,username):
    return render(request,'navAgent.html',locals()) 

def Redirect_centre(request,name):
    return render(request,'navCentre.html',locals()) 
