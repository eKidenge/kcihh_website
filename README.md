# Kenya Climate Innovation & Heritage Hub (KCIHH)

A comprehensive Django-based web platform for Kenya's leading youth-led climate action organization, bridging modern innovation with indigenous wisdom.

## Overview

KCIHH is a national youth-led platform advancing grassroots climate solutions across Kenya. The website serves as a digital hub for climate innovation, heritage preservation, community engagement, and impact tracking.

### Key Features

- **Youth-led climate action platform**
- **Innovation Hub** for climate startups
- **Indigenous Knowledge** preservation system
- **Training & Fellowship** programs
- **Community Action** initiatives
- **Impact tracking** dashboard
- **Blog/Insights** platform
- **Donation** gateway
- **Volunteer** management system
- **Resource library** with toolkits and publications

## Project Structure

## kcihh_website/

├── apps/
│ ├── home/ # Homepage and landing
│ ├── about/ # About Us page
│ ├── our_work/ # Our Work pages
│ │ ├── models.py # WorkCategory, SuccessStory
│ │ ├── views.py # our_work, work_category_detail
│ │ └── templates/
│ ├── impact/ # Impact tracking
│ │ ├── models.py # ImpactMetric, AnnualReport, CaseStudy, Testimonial
│ │ ├── views.py # ImpactListView, CaseStudy views
│ │ └── templates/
│ ├── get_involved/ # Volunteer, Donate, Partner pages
│ │ ├── models.py # InvolvementOption, VolunteerApplication, Donation
│ │ ├── views.py # get_involved, volunteer_application, donate
│ │ └── templates/
│ ├── resources/ # Resource library
│ │ ├── models.py # Resource, Category
│ │ ├── views.py # resources, resource_detail
│ │ └── templates/
│ ├── blog/ # Insights/Blog
│ │ ├── models.py # Category, Post, Comment
│ │ ├── views.py # blog_list, BlogDetailView
│ │ └── templates/
│ └── contact/ # Contact forms
│ ├── models.py # ContactMessage
│ ├── views.py # contact
│ └── templates/
├── static/ # Static files (CSS, JS, images)
├── media/ # User-uploaded media
├── templates/ # Base templates
│ └── includes/
│ ├── navigation.html # Main navigation bar
│ └── footer.html # Site footer
├── kcihh_website/ # Project configuration
│ ├── settings.py # Django settings
│ ├── urls.py # Main URL configuration
│ └── wsgi.py # WSGI configuration
├── manage.py
└── requirements.txt

## Installation

### Prerequisites

- Python 3.13+
- PostgreSQL with PostGIS
- pip (Python package manager)
- virtualenv (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/eKidenge/kcihh-website.git
cd kcihh-website
```

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
