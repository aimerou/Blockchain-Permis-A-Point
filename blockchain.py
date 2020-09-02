import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Blockchain.settings')
import django
django.setup()

from permis_a_point.models import *
from django.utils import timezone
import hashlib
import socket
import re
import sys

def NewBlock():
    date_debut = timezone.now()
    while (timezone.now() - date_debut).seconds <= 60:
        if (timezone.now() - date_debut).seconds == 60:
            transactions = []
            for t in Transaction.objects.all():
                if (timezone.now() - t.date).seconds < 60:
                    transactions.append(t)
            if len(transactions) > 0:
                new_block = Block()
                previous_block = Block.objects.latest()
                new_block.index = previous_block.index + 1
                new_block.previous_hash = previous_block.hash_block
                new_block.donnees = "" + str(transactions)
                to_hash = "" + str(transactions) + previous_block.hash_block
                new_block.hash_block = hashlib.sha256(to_hash.encode()).hexdigest()
                new_block.save()
                print("Nouveau block cree!")
            else:
                print("Aucune transaction n a ete effectuee, aucun nouveau bloc cree!")
            break

adress = "127.0.0.1"
port = 8080
s = socket.socket()
try:
    s.connect((adress, port))
    print ("\nConnecte a ", adress, " sur le port ", port, "; le serveur Django est actif!")
    while 1:
        NewBlock()
except socket.error:
    print ("Connection a ", adress, " sur le port ", port, " impossible; le serveur Django est inactif")
