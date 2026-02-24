# apps/get_involved/models.py
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class InvolvementOption(models.Model):
    OPTION_TYPES = [
        ('innovator', 'Youth Innovator'),
        ('volunteer', 'Volunteer'),
        ('community', 'Community Partner'),
        ('corporate', 'Corporate Sponsor'),
        ('donor', 'Donor'),
        ('researcher', 'Research Collaborator'),
    ]
    
    option_type = models.CharField(max_length=20, choices=OPTION_TYPES, unique=True)
    title = models.CharField(max_length=100)
    description = HTMLField()
    icon = models.ImageField(upload_to='involvement/')
    call_to_action = models.CharField(max_length=100)
    form_link = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class VolunteerApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    county = models.CharField(max_length=100)
    skills = models.TextField()
    motivation = models.TextField()
    availability = models.CharField(max_length=100)
    cv = models.FileField(upload_to='volunteer-cvs/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

class Donation(models.Model):
    FREQUENCY_CHOICES = [
        ('one_time', 'One Time'),
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]
    
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='KES')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    is_anonymous = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.amount} {self.currency}"