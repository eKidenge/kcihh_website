from django import forms
from .models import ContactSubmission, NewsletterSubscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'email', 'phone', 'organization', 
                  'inquiry_type', 'subject', 'message', 'newsletter_signup']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'newsletter_signup': forms.CheckboxInput(),
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email', 'first_name']