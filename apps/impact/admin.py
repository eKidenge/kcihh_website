from django.contrib import admin
from .models import ImpactMetric, AnnualReport, CaseStudy, Testimonial, ProjectLocation

@admin.register(ImpactMetric)
class ImpactMetricAdmin(admin.ModelAdmin):
    list_display = ['metric_type', 'current_value', 'updated_date']

@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'featured']
    list_filter = ['featured']

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'featured']
    list_filter = ['featured']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'location', 'featured', 'order']
    list_editable = ['order']

@admin.register(ProjectLocation)
class ProjectLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'project_type']
    list_filter = ['project_type', 'county']