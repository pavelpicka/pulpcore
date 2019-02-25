import os
from dynaconf.contrib import django_dynaconf
from django.conf import settings

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


if django_dynaconf.settings.get('MEDIA_ROOT') == '':
    media_root = '/var/lib/pulp'
else:
    media_root = django_dynaconf.settings.get('MEDIA_ROOT')

settings.__setattr__('MEDIA_ROOT', media_root)

if not django_dynaconf.settings.get('STATIC_ROOT'):
    settings.__setattr__('STATIC_ROOT', os.path.join(media_root, 'static/'))
