from django.shortcuts import render, get_object_or_404
from .models import WorkCategory

def our_work(request):
    categories = WorkCategory.objects.all()
    return render(request, 'our_work/index.html', {'categories': categories})

def work_category_detail(request, slug):
    category = get_object_or_404(WorkCategory, slug=slug)
    return render(request, 'our_work/detail.html', {'category': category})