# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

class User(AbstractUser):
    USER_TYPES = [
        ('youth', 'Youth Innovator'),
        ('elder', 'Community Elder'),
        ('partner', 'Partner Organization'),
        ('staff', 'KCIHH Staff'),
        ('admin', 'Administrator'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='youth')
    phone_number = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
    bio = models.TextField(blank=True)
    organization = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    country = CountryField(default='KE')
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Social links
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    # Email preferences
    newsletter_opt_in = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email