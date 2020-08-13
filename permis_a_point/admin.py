from django.contrib import admin
from .models import *

admin.site.register(Block)
admin.site.register(Permis)
admin.site.register(Conducteur)
admin.site.register(AgentSecurite)
admin.site.register(CentreStage)
admin.site.register(Attestation)
admin.site.register(Contravention)
admin.site.register(Transaction)