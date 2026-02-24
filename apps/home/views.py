from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HeroSection, Pillar, ImpactStat
from blog.models import Post

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = HeroSection.objects.filter(is_active=True).first()
        context['pillars'] = Pillar.objects.all().order_by('order')
        context['impact_stats'] = ImpactStat.objects.filter(is_active=True).order_by('order')
        context['latest_posts'] = Post.objects.filter(published=True).order_by('-published_date')[:3]
        return context