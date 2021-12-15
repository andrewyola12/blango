import os
from pathlib import Path
from configurations import Configuration
from configurations import values
import dj_database_url

class Dev(Configuration):
  
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = 'django-insecure-&!=9y436&^-bc$qia-mxngyf&xx)@ct)8lu@)=qxg_07-=z01w'

    DEBUG = True

    ALLOWED_HOSTS = ['*']
    X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
    CSRF_COOKIE_SAMESITE = None
    CSRF_TRUSTED_ORIGINS = [os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'blango_auth',
        'blog',
        'crispy_forms',
        'crispy_bootstrap5',
        'debug_toolbar',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'rest_framework',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    #   'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    #   'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'blango.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            "DIRS": [BASE_DIR / "templates"],
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

    WSGI_APPLICATION = 'blango.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

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

    PASSWORD_HASHERS = [
      'django.contrib.auth.hashers.Argon2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
      'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    LANGUAGE_CODE = 'en-us'
    ACCOUNT_ACTIVATION_DAYS = 7
    TIME_ZONE = values.Value("UTC")
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    SITE_ID = 1
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    INTERNAL_IPS = ["192.168.11.179"]
    
    STATIC_URL = '/static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    AUTH_USER_MODEL = "blango_auth.User"
    REGISTRATION_OPEN = True
class Prod(Dev):
    DEBUG = False