#!/bin/bash
# run_dev.sh

echo "Starting KCIHH Development Environment..."

# Set environment variables
export DJANGO_ENV=development
export DJANGO_SETTINGS_MODULE=kcihh_core.settings

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser if not exists
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@kcihh.org', 'admin123')"

# Load sample data
python manage.py loaddata sample_data.json

# Run development server
python manage.py runserver