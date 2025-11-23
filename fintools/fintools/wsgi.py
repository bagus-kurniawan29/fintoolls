import os
from django.core.wsgi import get_wsgi_application

# Pastikan ini 'fintoolls.settings' (sesuai nama folder)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fintools.settings')

app = application = get_wsgi_application()
