from django import forms
from .models import VolunteerApplication, Donation

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'phone', 'date_of_birth', 'county', 
                  'skills', 'motivation', 'availability', 'cv']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.Textarea(attrs={'rows': 4}),
            'motivation': forms.Textarea(attrs={'rows': 4}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'currency', 'frequency', 'full_name', 'email', 
                  'phone', 'is_anonymous', 'payment_method']
        widgets = {
            'is_anonymous': forms.CheckboxInput(),
        }