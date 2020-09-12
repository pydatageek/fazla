"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# assets directory -> templates, static, media
ASSETS_DIR = BASE_DIR / 'assets'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(BASE_DIR / 'secrets.json') as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost', '.localhost',
    'fazla.net', '.fazla.net', '178.62.30.148']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # for compression

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'crum',  # to get current_user on model save
    'rest_framework',
    'import_export',
    'imagekit',  # for image thumbnails
    'ckeditor',  # wysiwyg editor -> requires ./manage.py collectstatic
    'widget_tweaks',

    'core',
    'accounts',
    'sources',
    'places',
    'politics',
    'info',
    'stats',

    'compressor',  # for compression
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for compression
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'crum.CurrentRequestUserMiddleware',  # to get current_user on model save

    "compression_middleware.middleware.CompressionMiddleware",  # for compression
]

if DEBUG:
    MIDDLEWARE += [
        # debug_toolbar for debug=True
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            ASSETS_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',  # for localization
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': get_secret('DB_LOCAL_NAME'),
    #     'USER': get_secret('DB_LOCAL_UNAME'),
    #     'PASSWORD': get_secret('DB_LOCAL_PASS'),
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_REMOTE_NAME'),
        'USER': get_secret('DB_REMOTE_UNAME'),
        'PASSWORD': get_secret('DB_REMOTE_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True

DATE_INPUT_FORMATS = [
    '%b %d %Y',  # 'Oct 25 2020'
    '%b %d, %Y',  # 'Oct 25, 2020'
    '%d %b %Y',  # '25 Oct 2020'
    '%d %b, %Y',  # '25 Oct, 2020'
    '%B %d %Y',  # 'October 25 2020'
    '%B %d, %Y',  # 'October 25, 2020'
    '%d %B %Y',  # '25 October 2020'
    '%d %B, %Y',  # '25 October, 2020'
    '%d.%m.%Y',  # '25.10.2020'
    '%d/%m/%Y',  # '25/10/2020'
    '%d-%m-%Y',  # '25-10-2020'
    '%Y.%m.%d',  # '2020.10.25'
    '%Y-%m-%d',  # '2020-10-25'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    ASSETS_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = ASSETS_DIR / 'media'

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# rest_framework related
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# ckeditor related
# CKEDITOR_BASEPATH = '/assets/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    # 'awesome_ckeditor': {
    #     'toolbar': 'Basic',
    # },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}

if DEBUG:
    # debug_toolbar for debug=True
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

SITE_ID = 1

DATA_UPLOAD_MAX_NUMBER_FIELDS = 40000


# for compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Whitenoise cache policy
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)

COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True if DEBUG == False else False

COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
    "js": ["compressor.filters.jsmin.JSMinFilter"],
}

"""
# for compression
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)
# COMPRESS_ENABLED = True

# redis configuration: for cache
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# Cache time to live is 5 minutes
CACHE_TTL = 60 * 5

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
"""
