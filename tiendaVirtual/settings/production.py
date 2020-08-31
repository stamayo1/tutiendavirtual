from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tutiendavirual.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd61rgtuu97u3u2',
        'USER': 'yskvwdsixpydkm',
        'PASSWORD': 'cef0457216c1ae34377103902d824b94d22ada7f1e6cdcd5c6e41a63554545ad',
        'HOST': 'ec2-54-243-67-199.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')