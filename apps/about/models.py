from django.db import models
from tinymce.models import HTMLField

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class AdvisoryBoard(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='advisory/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Partner(models.Model):
    PARTNER_TYPES = [
        ('corporate', 'Corporate'),
        ('ngo', 'NGO'),
        ('government', 'Government'),
        ('community', 'Community'),
        ('academic', 'Academic'),
    ]
    
    name = models.CharField(max_length=200)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name