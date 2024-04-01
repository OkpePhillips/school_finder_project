"""
WSGI config for sch_finder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv  # Import load_dotenv function
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sch_finder.settings')

# Load environment variables from .env file
load_dotenv()

application = get_wsgi_application()
