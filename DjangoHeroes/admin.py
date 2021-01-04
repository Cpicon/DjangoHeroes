from django.contrib import admin

#models
from .models import *

#utils
from django.db.models import Count
# Register your models here.
admin.site.register(Hero)
admin.site.register(Villain)

admin.site.register(Category)

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):

    # optimize the number of query by modifying the queryset of ModelAmin.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        """Annotate porque estó reduce los queries """
        queryset = queryset.annotate(
            _hero_count= Count('hero', distinct=True),
            _villain_count= Count('villain', distinct=True)
        )
        return queryset

    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villain_set.count()
    list_display = ('name', 'hero_count', 'villain_count')