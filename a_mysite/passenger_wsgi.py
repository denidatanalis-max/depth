import os
import sys

try:
    BASE_DIR = '/home/unitestm/django-app'
    sys.path.insert(0, BASE_DIR)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'a_mysite.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

except Exception as e:
    with open('/home/unitestm/logs/passenger_error.log', 'a') as f:
        f.write(str(e) + '\n')
    raise