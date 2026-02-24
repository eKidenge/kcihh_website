# gunicorn.conf.py
import multiprocessing
import os

# Bind to socket
bind = "127.0.0.1:8000"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Process naming
proc_name = "kcihh_core"

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Server mechanics
daemon = False
pidfile = "/var/run/gunicorn/kcihh.pid"
umask = 0o007
user = "www-data"
group = "www-data"

# SSL (if terminating at gunicorn instead of nginx)
# keyfile = "/etc/ssl/private/kcihh.org.key"
# certfile = "/etc/ssl/certs/kcihh.org.crt"

# Django settings
raw_env = [
    "DJANGO_SETTINGS_MODULE=kcihh_core.settings",
    "DJANGO_ENV=production",
]

# Preload application
preload_app = True

def on_starting(server):
    """Log when server starts."""
    server.log.info("Starting KCIHH Gunicorn server.")

def on_reload(server):
    """Log when server reloads."""
    server.log.info("Reloading KCIHH Gunicorn server.")

def when_ready(server):
    """Log when server is ready."""
    server.log.info("KCIHH Gunicorn server is ready.")

def on_exit(server):
    """Log when server exits."""
    server.log.info("Stopping KCIHH Gunicorn server.")