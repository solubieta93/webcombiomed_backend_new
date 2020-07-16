"""
Django settings for web_api project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR, 'BASE_DIR')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'e%a(a!f#gw==ss*=+xny0w(87*d7xuixhpa3ndn%ftw&-)j+k-'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# SECURITY WARNING: don't run with debug turned on in production!
# TODO: COMMENT TO USE IN PRODUCTION MODE
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
# TODO: UNCOMMENT TO USE IN PRODUCTION MODE
DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

# TODO: ADD HOST
ALLOWED_HOSTS = ['api-combiomed.herokuapp.com', 'localhost', '127.0.0.1', '192.168.2.102']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # TODO: UNCOMMENT TO USE IN DEVELOPMENT MODE
    # 'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'products',
    'rest_framework',
    'knox',
    'accounts',
    'blog',
    'contacts',
    'chat',
    'corsheaders',
    'django_filters',
    'files',
    'mails',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',
         # 'rest_framework.permissions.IsAuthenticated',
         ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # TODO: UNCOMMENT TO USE IN PRODUCTION MODE
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'web_api.custom_cache.DisableClientSideCachingMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8080",
    "http://192.168.2.102:8080"
)
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'web_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'heroku_db': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'combiomed',
        'HOST': 'mongodb://localhost:27017/combiomed',
        # 'USER': '<dbuser>',
        # 'PASSWORD': '<dbpassword>',
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# TODO: UNCOMMENT TO USE IN PRODUCTION MODE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# TODO: if dont work uncomment above
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# #  Add configuration for static files storage using whitenoise
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'solubieta93@gmail.com'
EMAIL_HOST_PASSWORD = 'Sol@93092305534'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = False

# UNCOMMENT TO USE HEROKU
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['heroku_db'].update(db_from_env)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self",)
CSP_SCRIPT_SRC = ("'self",)
CSP_FONT_SRC = ("'self",)
CSP_IMG_SRC = ("'self",)