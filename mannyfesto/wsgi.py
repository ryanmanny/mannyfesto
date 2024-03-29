"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/mannyfesto')
load_dotenv(os.path.join(project_folder, '.env'), override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mannyfesto.settings')

application = get_wsgi_application()
