# apps/resources/models.py
from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class ResourceType(models.Model):
    TYPE_CHOICES = [
        ('toolkit', 'Climate Toolkit'),
        ('research', 'Research Paper'),
        ('policy', 'Policy Brief'),
        ('indigenous', 'Indigenous Knowledge Publication'),
        ('manual', 'Training Manual'),
        ('funding', 'Funding Opportunity'),
        ('data', 'Climate Data Resource'),
    ]
    
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True)
    description = HTMLField()
    file = models.FileField(upload_to='resources/', blank=True)
    external_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='resources/covers/', blank=True)
    author = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    published_date = models.DateField()
    language = models.CharField(max_length=50, default='English')
    download_count = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)