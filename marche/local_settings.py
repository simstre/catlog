import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marche',
        'USER': 'marche_app',
        'PASSWORD': 'hwrk779',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
