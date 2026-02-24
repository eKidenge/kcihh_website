# apps/impact/urls.py
from django.urls import path
from . import views

#app_name = 'impact'  # Add this line to register the namespace

urlpatterns = [
    # Main impact page - using the class-based view
    path('', views.ImpactListView.as_view(), name='impact'),
    path('', views.ImpactListView.as_view(), name='impact_list'),  # Change from 'impact' to 'impact_list'
    # API endpoint for map data - using the correct function name from your views
    path('map-data/', views.get_project_locations_api, name='map_data'),
    
    # Case study URLs
    path('case-studies/', views.CaseStudyListView.as_view(), name='case_study_list'),
    path('case-studies/<slug:slug>/', views.CaseStudyDetailView.as_view(), name='case_study_detail'),
    
    # Testimonial URLs
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    
    # Annual report URLs
    path('reports/', views.AnnualReportListView.as_view(), name='report_list'),
    path('reports/<int:year>/', views.AnnualReportDetailView.as_view(), name='report_detail'),
    path('reports/<int:year>/download/', views.download_report, name='download_report'),
    
    # API endpoints
    path('api/metrics/', views.get_metrics_api, name='metrics_api'),
    path('api/locations/', views.get_project_locations_api, name='locations_api'),
    
    # Dashboard (staff only)
    path('dashboard/', views.impact_dashboard, name='dashboard'),
]