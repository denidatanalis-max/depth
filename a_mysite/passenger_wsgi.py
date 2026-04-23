import os
import sys

sys.path.insert(0, '/home/unitestm/django-app')
sys.path.insert(0, '/home/unitestm/django-app/a_mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'a_mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()