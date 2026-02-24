# apps/impact/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Sum, Count, Q
from django.http import JsonResponse, HttpResponse
from .models import ImpactMetric, AnnualReport, CaseStudy, Testimonial, ProjectLocation
import json

# Fix the ImpactListView - it needs a model or queryset
class ImpactListView(ListView):
    """Main impact page showing all impact data"""
    model = ImpactMetric  # Add this line to specify the model
    template_name = 'impact/impact_list.html'
    context_object_name = 'metrics'  # This will be available in template as 'metrics'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all metrics (already provided by the ListView, but we can add more context)
        context['metrics'] = ImpactMetric.objects.all()
        
        # Get featured case studies
        context['case_studies'] = CaseStudy.objects.filter(featured=True)[:6]
        
        # Get featured testimonials
        context['testimonials'] = Testimonial.objects.filter(featured=True)[:6]
        
        # Get recent annual reports
        context['reports'] = AnnualReport.objects.all()[:3]
        
        # Calculate total impact statistics
        context['total_stats'] = {
            'total_beneficiaries': ImpactMetric.objects.filter(
                metric_type__in=['youth', 'households']
            ).aggregate(total=Sum('current_value'))['total'] or 0,
            'total_trees': ImpactMetric.objects.filter(
                metric_type='trees'
            ).aggregate(total=Sum('current_value'))['total'] or 0,
            'total_land': ImpactMetric.objects.filter(
                metric_type='land'
            ).aggregate(total=Sum('current_value'))['total'] or 0,
            'total_enterprises': ImpactMetric.objects.filter(
                metric_type='enterprise'
            ).aggregate(total=Sum('current_value'))['total'] or 0,
        }
        
        return context

# Alternative: If you don't want to use model, override get_queryset
"""
class ImpactListView(ListView):
    template_name = 'impact/impact_list.html'
    context_object_name = 'metrics'
    
    def get_queryset(self):
        return ImpactMetric.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Rest of your context data
        return context
"""

# Case Study Views
class CaseStudyListView(ListView):
    """View for listing all case studies"""
    model = CaseStudy
    template_name = 'impact/case_study_list.html'
    context_object_name = 'case_studies'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = CaseStudy.objects.all()
        
        # Filter by sector if provided
        sector = self.request.GET.get('sector')
        if sector:
            queryset = queryset.filter(sector=sector)
        
        # Search functionality
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(challenge__icontains=search_query)
            )
        
        return queryset.order_by('-published_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sectors'] = CaseStudy.SECTOR_CHOICES
        context['current_sector'] = self.request.GET.get('sector', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context

class CaseStudyDetailView(DetailView):
    """View for individual case study"""
    model = CaseStudy
    template_name = 'impact/case_study_detail.html'
    context_object_name = 'case_study'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related case studies (same sector or location)
        context['related_case_studies'] = CaseStudy.objects.filter(
            Q(sector=self.object.sector) | Q(location=self.object.location)
        ).exclude(id=self.object.id)[:3]
        return context

# Testimonial Views
class TestimonialListView(ListView):
    """View for listing all testimonials"""
    model = Testimonial
    template_name = 'impact/testimonial_list.html'
    context_object_name = 'testimonials'
    paginate_by = 12
    
    def get_queryset(self):
        return Testimonial.objects.all().order_by('order', '-id')

# Annual Report Views
class AnnualReportListView(ListView):
    """View for listing all annual reports"""
    model = AnnualReport
    template_name = 'impact/report_list.html'
    context_object_name = 'reports'
    paginate_by = 6
    
    def get_queryset(self):
        return AnnualReport.objects.all().order_by('-year')

class AnnualReportDetailView(DetailView):
    """View for individual annual report"""
    model = AnnualReport
    template_name = 'impact/report_detail.html'
    context_object_name = 'report'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get other reports
        context['other_reports'] = AnnualReport.objects.exclude(
            id=self.object.id
        ).order_by('-year')[:3]
        return context

def download_report(request, year):
    """Handle report download and count increment"""
    report = get_object_or_404(AnnualReport, year=year)
    
    # Increment download count
    report.increment_download_count()
    
    # Serve the file
    response = HttpResponse(report.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report.title}_{year}.pdf"'
    return response

# API Endpoints for AJAX requests
def get_metrics_api(request):
    """API endpoint for fetching metrics data"""
    metrics = ImpactMetric.objects.all()
    data = []
    
    for metric in metrics:
        data.append({
            'type': metric.get_metric_type_display(),
            'value': metric.current_value,
            'target': metric.target_value,
            'unit': metric.unit,
            'color': metric.color,
            'icon': metric.icon,
            'progress': metric.get_progress_percentage() if hasattr(metric, 'get_progress_percentage') else None,
        })
    
    return JsonResponse({'metrics': data})

def get_project_locations_api(request):
    """API endpoint for project locations (for maps)"""
    locations = ProjectLocation.objects.filter(is_active=True)
    data = []
    
    for location in locations:
        data.append({
            'name': location.name,
            'type': location.get_project_type_display(),
            'county': location.county,
            'lat': location.coordinates.y if location.coordinates else None,
            'lng': location.coordinates.x if location.coordinates else None,
            'beneficiaries': location.beneficiaries,
            'description': location.description[:200],
            'image_url': location.image.url if location.image else None,
        })
    
    return JsonResponse({'locations': data})

# Dashboard View (for admin/staff)
def impact_dashboard(request):
    """Admin dashboard for impact visualization"""
    if not request.user.is_staff:
        return HttpResponse(status=403)
    
    # Aggregate data for charts
    metrics_by_type = ImpactMetric.objects.values('metric_type').annotate(
        total=Sum('current_value')
    )
    
    # Case studies by sector
    case_studies_by_sector = CaseStudy.objects.values('sector').annotate(
        count=Count('id')
    )
    
    # Testimonials by location
    testimonials_by_location = Testimonial.objects.values('location').annotate(
        count=Count('id')
    )
    
    context = {
        'metrics_by_type': json.dumps(list(metrics_by_type)),
        'case_studies_by_sector': json.dumps(list(case_studies_by_sector)),
        'testimonials_by_location': json.dumps(list(testimonials_by_location)),
        'total_metrics': ImpactMetric.objects.count(),
        'total_case_studies': CaseStudy.objects.count(),
        'total_testimonials': Testimonial.objects.count(),
        'total_reports': AnnualReport.objects.count(),
    }
    
    return render(request, 'impact/dashboard.html', context)