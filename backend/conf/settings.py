import os
from datetime import timedelta
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

from .utils import RemoveEscapeSequencesFilter

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

RESET_INVITE_SECRET_KEY = os.getenv('DJANGO_RESET_INVITE_SECRET_KEY')

DEV_SERVICES = os.getenv('DEV_SERVICES', False) == 'True'

DEBUG = os.getenv('DJANGO_DEBUG', False) == 'True'

ALLOWED_HOSTS = [os.getenv('DJANGO_ALLOWED_HOSTS', default='*')]

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
    'django_filters',
    'debug_toolbar',
    'phonenumber_field',
    'djoser',
    'drf_yasg',
    'corsheaders',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',

    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'socials.apps.SocialsConfig',
    'events.apps.EventsConfig',
    'metrics.apps.MetricsConfig',
    'notifications.apps.NotificationsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'

ASGI_APPLICATION = 'conf.asgi.application'

ELASTIC_HOST = os.getenv('ELASTIC_HOST', default='localhost')

ELASTIC_PORT = os.getenv('ELASTIC_PORT', default='9200')

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': f'{ELASTIC_HOST}:{ELASTIC_PORT}'
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (os.getenv('REDIS_HOST', default='localhost'),
                 os.getenv('REDIS_PORT', default='6379'))
            ],
        },
    }
}

DJOSER = {
    'LOGIN_FIELD': 'email'
}

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default='5432')
    }
}

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
    {'NAME': 'users.validators.UppercasePasswordValidator', 'OPTIONS': {'min_count': 1}, },
    {'NAME': 'users.validators.LowercasePasswordValidator', 'OPTIONS': {'min_count': 1}, },
    {'NAME': 'users.validators.NoSpacesPasswordValidator', },
    {'NAME': 'users.validators.MaximumLengthPasswordValidator', },
    {'NAME': 'users.validators.AllowOnlyThisCharactersValidator', },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'TOKEN_OBTAIN_SERIALIZER': 'api.v1.users.serializers.CustomTokenObtainSerializer',
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'DEFAULT_MODEL_RENDERING': 'example'
}

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

DJANGO_SMTP = os.getenv('DJANGO_SMTP', False) == 'True'

if DJANGO_SMTP:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_PORT = 465

EMAIL_USE_TLS = False

EMAIL_USE_SSL = True

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

# ----------------------------------------------------------------

INVITE_TIME_EXPIRES_DAYS = 7

CORS_ORIGIN_ALLOW_ALL = True

if DEBUG is False:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # Setup support for proxy headers
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF_TRUSTED_ORIGINS = []

if DEV_SERVICES:

    log_dir = os.path.join(BASE_DIR, 'logs')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'error.log')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'WARNING',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': log_file,
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 1,
                'formatter': 'verbose',
                'filters': ['remove_escape_sequences'],
            },
        },
        'filters': {
            'remove_escape_sequences': {
                '()': RemoveEscapeSequencesFilter,
            },
        },
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s',
            },
            'verbose': {
                'format': '%(asctime)s %(levelname)s [%(process)d] %(name)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

    SENTRY_DSN = os.getenv('SENTRY_DSN')

    if SENTRY_DSN:
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            integrations=[DjangoIntegration()],
            traces_sample_rate=1.0,
            send_default_pii=True
        )
