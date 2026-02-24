# apps/home/models.py
from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class HeroSection(models.Model):
    headline = models.CharField(max_length=200, default="Youth-Led. Community-Driven. Climate Solutions for Kenya.")
    subheading = models.TextField(max_length=500, default="We incubate climate innovations, preserve indigenous knowledge...")
    primary_cta_text = models.CharField(max_length=50, default="Join the Movement")
    secondary_cta_text = models.CharField(max_length=50, default="Partner with Us")
    background_image = models.ImageField(upload_to='hero/')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

class Pillar(models.Model):
    ICON_CHOICES = [
        ('lab', 'Innovation Lab'),
        ('heritage', 'Indigenous Knowledge'),
        ('training', 'Training'),
        ('community', 'Community Action'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    icon_image = models.ImageField(upload_to='pillars/', blank=True)
    link = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class ImpactStat(models.Model):
    label = models.CharField(max_length=100)  # "Youth trained", "Trees planted"
    value = models.IntegerField()  # 500, 50000
    suffix = models.CharField(max_length=20, blank=True, default='+')  # +, K, M
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.value}{self.suffix} {self.label}"