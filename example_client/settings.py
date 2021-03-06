
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'v)p5g44bi$i315*edao%--11$!)_c1)l9ab%e4f2a!agx5bry='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.1.2']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'example_client.urls'

WSGI_APPLICATION = 'example_client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

OAUTH = {
    'AUTHORIZE_URI': 'http://127.0.1.1/oauth2/authorize/',
    'TOKEN_URI': 'http://127.0.1.1/oauth2/token/',
    'API_URI': 'http://127.0.1.1/api/user/',
    'CLIENT_ID': '7dya49SJdYbTcG9ej7Jj-UGe-e.fQZDW5YnbdKfy',
    'CLIENT_SECRET': 'SHOeXsB6PtExT23JpR2CNJsEkAKdvk7XZPGA2hxm-iIH@UM@_lwX9fFl!ZINBWWQsu1T90lgGwhsPYuJlzXp0nki@K6EoTggQUbi11HHB.P9mYq!!wyk92:QdQVzy9sQ',
    'REDIRECT_URI': 'http://127.0.1.2/passport/',
}

AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/login/'

