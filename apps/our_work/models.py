# apps/our_work/models.py
from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

class WorkCategory(models.Model):
    CATEGORY_TYPES = [
        ('innovation', 'Innovation Hub'),
        ('indigenous', 'Indigenous Knowledge'),
        ('training', 'Training & Fellowship'),
        ('community', 'Community Action'),
    ]
    
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES, unique=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=300)
    featured_image = models.ImageField(upload_to='work/categories/')
    icon = models.ImageField(upload_to='work/icons/')
    content = HTMLField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('work_category_detail', args=[self.slug])

class FocusArea(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE, related_name='focus_areas')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.category.title} - {self.title}"

class Program(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE, related_name='programs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100, blank=True)
    eligibility = models.TextField(blank=True)
    application_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(WorkCategory, on_delete=models.SET_NULL, null=True, blank=True)
    person_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    quote = models.TextField()
    story = HTMLField()
    image = models.ImageField(upload_to='stories/')
    video_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title