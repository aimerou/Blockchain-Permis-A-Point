from django.shortcuts import render

def Accueil(request):
    return render(request,'accueil.html')

def Inscription(request):
    return render(request,'inscription.html')

def Connexion(request):
    return render(request,'connexion.html')

def DashboardConducteur(request):
    return render(request,'dashboardConducteur.html')

def DashboardAgentSecurite(request):
    return render(request,'dashboardAgentSecurite.html')

def DashboardCentreStage(request):
    return render(request,'dashboardCentreStage.html')

