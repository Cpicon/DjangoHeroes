from django.contrib.admin import AdminSite
# DjangoEvents models
from .models import *
# Register your models here.

class EventAdminSite(AdminSite):

    site_header = 'DjangoHeroes administration'
    index_title = 'Events administration'
    site_title = 'Django Heroes Events admin'

event_admin_site = EventAdminSite(name='event_admin')

event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)