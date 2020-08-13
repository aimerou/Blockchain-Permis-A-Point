import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Blockchain.settings')
import django
django.setup()

from permis_a_point.models import Block
import hashlib

GenesisBlock = Block()
GenesisBlock.index = 1
GenesisBlock.previous_hash = "NIL"
GenesisBlock.donnees = "Ceci est le premier bloc de la blockchain; il ne contient aucune transaction!"
GenesisBlock.hash_block = hashlib.sha256(GenesisBlock.donnees.encode()).hexdigest()
GenesisBlock.save()