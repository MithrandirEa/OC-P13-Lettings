from django.contrib import admin

# TODO: à séparer en deux admin.py différents dans les apps lettings et profiles
from .models import Letting
from .models import Address
from .models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
