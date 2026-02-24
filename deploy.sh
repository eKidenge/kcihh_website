#!/bin/bash
# deploy_prod.sh

echo "Deploying KCIHH to Production..."

# Set environment
export DJANGO_ENV=production
export DJANGO_SETTINGS_MODULE=kcihh_core.settings

# Pull latest code
git pull origin main

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Clear cache
python manage.py clear_cache

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart celery
sudo systemctl restart celery-beat
sudo systemctl reload nginx

# Check status
sudo systemctl status gunicorn --no-pager
sudo systemctl status celery --no-pager

echo "Deployment complete!"