from django.contrib import admin
from .clases.usuarios import Usuario
from .clases.coin import Coin

admin.site.register(Usuario)
admin.site.register(Coin)
