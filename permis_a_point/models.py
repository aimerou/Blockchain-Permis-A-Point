from djongo import models

class Block(models.Model):
    index = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donnees = models.TextField()
    previous_hash = models.CharField(max_length=1000,default="NIL")
    hash_block = models.CharField(max_length=1000)
    class Meta:
        ordering = ['index']
        get_latest_by = "index"

class Permis(models.Model):
    prenom = models.CharField(max_length=60)
    nom = models.CharField(max_length=40)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=40)
    date_delivrance = models.DateField()
    date_expiration = models.DateField()
    numero = models.IntegerField()
    groupe_sanguin = models.CharField(max_length=3)
    categorie_vehicule = models.CharField(max_length=2)

class Conducteur(models.Model):
    conducteur = models.ForeignKey('Permis',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=15,default="conducteur")
    password = models.CharField(max_length=255,default="passer") 

class AgentSecurite(models.Model):
    username=models.CharField(max_length=15,default="agent")
    prenom = models.CharField(max_length=60)
    nom = models.CharField(max_length=40)
    matricule = models.IntegerField()
    password = models.CharField(max_length=255,default="passer")

class CentreStage(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=40)
    password = models.CharField(max_length=255,default="passer")

class Attestation(models.Model):
    centre = models.ForeignKey('CentreStage',on_delete=models.CASCADE)
    stagiaire = models.ForeignKey('Conducteur',on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    contenu = models.TextField()

class Contravention(models.Model):
    agent = models.ForeignKey('AgentSecurite',on_delete=models.CASCADE)
    destinataire = models.ForeignKey('Conducteur',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    categorie = models.IntegerField()
    contenu = models.TextField()

class Transaction(models.Model):
    conducteur = models.ForeignKey('Conducteur',on_delete=models.CASCADE)
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return " {} {} a reçu {} points à la date {} ".format(self.conducteur.conducteur.prenom,self.conducteur.conducteur.nom, self.points, self.date)
