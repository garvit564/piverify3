"""
WSGI config for pi_clone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi_clone.settings')

application = get_wsgi_application()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
