from django.contrib import admin
from .models import Agencia
from .models import Persona
from .models import Empleo
from .models import Rubro
from .models import Oferta
from .models import Empresa

admin.site.register(Agencia)
admin.site.register(Persona)
admin.site.register(Empleo)
admin.site.register(Rubro)
admin.site.register(Oferta)
admin.site.register(Empresa)
