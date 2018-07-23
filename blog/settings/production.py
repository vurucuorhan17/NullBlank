from blog.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nullblank',
        'USER': 'nulluser',
        'PASSWORD': 'NullBlank',
        'HOST': 'localhost',
        'PORT': '',

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')