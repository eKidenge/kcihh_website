from django.shortcuts import render, redirect
from .models import ContactSubmission, NewsletterSubscriber
from .forms import ContactForm, NewsletterForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {'form': form})

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        NewsletterSubscriber.objects.get_or_create(email=email)
    return redirect('home')