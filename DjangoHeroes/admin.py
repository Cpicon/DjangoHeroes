from django.contrib import admin

#models
from .models import *

# Register your models here.
admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(Origin)
admin.site.register(Category)

