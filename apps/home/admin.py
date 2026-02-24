from django.contrib import admin
from .models import HeroSection, Pillar, ImpactStat

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['headline', 'is_active']
    list_filter = ['is_active']

@admin.register(Pillar)
class PillarAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'order']
    list_editable = ['order']