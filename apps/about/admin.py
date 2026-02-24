from django.contrib import admin
from .models import TeamMember, AdvisoryBoard, Partner

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order']
    list_editable = ['order']

@admin.register(AdvisoryBoard)
class AdvisoryBoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'partner_type']