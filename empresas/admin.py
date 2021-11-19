from django.contrib import admin
from .models import Tipo_Negocio
from .models import Negocio
from .models import Evento
from .models import SiteAreas
from .models import Atracoe
# Register your models here.

admin.site.register(Tipo_Negocio)
admin.site.register(Negocio)
admin.site.register(Evento)
admin.site.register(SiteAreas)
admin.site.register(Atracoe)