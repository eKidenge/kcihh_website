from django.shortcuts import render

def about(request):
    return render(request, 'about/index.html')

def team(request):  # Add this function
    return render(request, 'about/team.html')  # You'll need to create this template