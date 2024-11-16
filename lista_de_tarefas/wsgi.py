"""
WSGI config for lista_de_tarefas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from lista_de_tarefas.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lista_de_tarefas.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

app = application
