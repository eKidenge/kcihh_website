# apps/impact/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField
from tinymce.models import HTMLField

class ImpactMetric(models.Model):
    METRIC_TYPES = [
        ('youth', 'Youth & Farmers Trained'),
        ('enterprise', 'Enterprises Launched'),
        ('emissions', 'Emissions Reduced (tCO2e)'),
        ('land', 'Land Restored (acres)'),
        ('households', 'Households Reached'),
        ('indigenous', 'Indigenous Practices Documented'),
        ('jobs', 'Jobs Created'),
        ('trees', 'Trees Planted'),
    ]
    
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES, unique=True)
    current_value = models.IntegerField()
    target_value = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True)  # acres, tCO2e, etc.
    icon = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default="#10B981")  # Tailwind color
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_metric_type_display()}: {self.current_value}"

class AnnualReport(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(unique=True)
    summary = HTMLField()
    pdf_file = models.FileField(upload_to='reports/')
    cover_image = models.ImageField(upload_to='reports/covers/')
    featured = models.BooleanField(default=False)
    download_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.title} ({self.year})"

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    challenge = HTMLField()
    solution = HTMLField()
    impact = HTMLField()
    image = models.ImageField(upload_to='case-studies/')
    video_url = models.URLField(blank=True)
    published_date = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    person_name = models.CharField(max_length=100)
    person_role = models.CharField(max_length=100)  # "Youth Innovator", "Community Elder"
    location = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    video_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.person_name} - {self.location}"
    
    # apps/impact/models.py (continued)
from django.contrib.gis.db import models as gis_models

class ProjectLocation(models.Model):
    PROJECT_TYPES = [
        ('innovation', 'Innovation Hub'),
        ('restoration', 'Ecosystem Restoration'),
        ('water', 'Water Harvesting'),
        ('training', 'Training Site'),
        ('seed_bank', 'Community Seed Bank'),
    ]
    
    name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    county = models.CharField(max_length=100)
    #coordinates = gis_models.PointField(srid=4326)  # For GeoDjango
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='project-locations/')
    beneficiaries = models.IntegerField(default=0)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.county}"