from django.contrib import admin

# models
from .models import *

# utils
from django.db.models import Count

# Register your models here.
admin.site.register(Villain)

admin.site.register(Category)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):

    # optimize the number of query by modifying the queryset of ModelAmin.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        """Annotate porque estó reduce los queries """
        queryset = queryset.annotate(
            _hero_count=Count('hero', distinct=True),
            _villain_count=Count('villain', distinct=True)
        )
        return queryset

    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villain_set.count()

    list_display = ('name', 'hero_count', 'villain_count')

    #allow order the Origin admin section by calculated fields that are not present in Origin model
    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'

class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'is very benevolent'
    parameter_name = 'is_very_benevolent'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'yes'),
            ('No', 'No')
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(benevolence_factor__gt=75)
        else:
            return queryset.filter(benevolence_factor__gt=75)
        return queryset

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    
    def is_very_benevolent(self, obj):
        return obj.benevolence_factor >75
    

    
    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)


